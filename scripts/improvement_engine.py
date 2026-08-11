#!/usr/bin/env python3
from pathlib import Path
from collections import Counter, defaultdict
import argparse, json, copy

FAILURES={
"WRONG_INTENT","DOMAIN_MISROUTE","OVERTHINKING","UNDERTHINKING","STOP_FAILURE","NO_CLEAR_RECOMMENDATION","NO_NEXT_ACTION",
"EVIDENCE_MISS","WRONG_SOURCE","FALSE_CERTAINTY","DUPLICATE_EVIDENCE","RED_TEAM_FALSE_POSITIVE","RED_TEAM_FALSE_NEGATIVE",
"STRAWMAN_CHALLENGE","TOOL_OVERUSE","TOOL_UNDERUSE","TOOL_WRONG_FIRST_CALL","TOOL_REPEAT","READ_BEFORE_WRITE","ACTION_SCOPE",
"ACTION_NOT_VERIFIED","STATE_DRIFT","HINDSIGHT_REWRITE","OVER_UPDATE","UNDER_UPDATE","CRITERION_DRIFT","STALE_STATE",
"EVAL_BUG","PARSER_BUG","CAPABILITY_LIMIT","AMBIGUOUS_INPUT"
}
SEVERITY={"P0","P1","P2","P3"}
PROPOSAL_STATES={"captured","triaged","pattern_confirmed","candidate","testing","ready_for_review","rejected","promoted","rolled_back"}

def load(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def save(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def validate_record(r):
    e=[]
    if not isinstance(r,dict):
        return ["record:not-object"]
    if r.get("schema_version")!="1.6":e.append("schema_version")
    collections={}
    for f in ("incidents","patterns","proposals","releases"):
        v=r.get(f)
        if not isinstance(v,list):
            e.append(f"{f}:not-list")
            collections[f]=[]
        else:
            collections[f]=v
    ids=[]
    for i in collections["incidents"]:
        if not isinstance(i,dict):
            e.append("incident:not-object")
            continue
        if not i.get("incident_id"):e.append("incident missing id")
        if i.get("failure_type") not in FAILURES:e.append(f"{i.get('incident_id')}:failure_type")
        if i.get("severity") not in SEVERITY:e.append(f"{i.get('incident_id')}:severity")
        ids.append(i.get("incident_id"))
    if len(ids)!=len(set(ids)):e.append("duplicate incident_id")
    pids=[]
    for p in collections["proposals"]:
        if not isinstance(p,dict):
            e.append("proposal:not-object")
            continue
        pids.append(p.get("proposal_id"))
        if p.get("status") not in PROPOSAL_STATES:e.append(f"{p.get('proposal_id')}:status")
    if len(pids)!=len(set(pids)):e.append("duplicate proposal_id")
    return e

def detect_patterns(r):
    groups=defaultdict(list)
    for i in r["incidents"]:
        if i.get("pattern_key"):groups[i["pattern_key"]].append(i)
    out=[]
    for key,incs in sorted(groups.items()):
        forms={i.get("prompt_form") for i in incs if i.get("prompt_form")}
        critical=any(i["severity"] in ("P0","P1") for i in incs)
        repro=any(bool(i.get("reproducible")) for i in incs)
        normal=len(incs)>=3 and len(forms)>=2 and repro
        status="pattern_confirmed" if (normal or critical) else "insufficient_evidence"
        out.append({
            "pattern_key":key,"incident_ids":[i["incident_id"] for i in incs],"count":len(incs),
            "distinct_prompt_forms":len(forms),"critical_escalation":critical,"reproducible":repro,"status":status
        })
    return out

def proposal_quality(p):
    required=["proposal_id","pattern_key","target_layer","target_files","current_rule","proposed_rule","general_rationale",
              "supporting_incident_ids","expected_improvements","predicted_regression_risks","required_eval_suites","rollback_plan"]
    missing=[k for k in required if not p.get(k)]
    exact_patch=bool(p.get("exact_prompt_patch"))
    evaluable=bool(p.get("required_eval_suites"))
    rollback=bool(p.get("rollback_plan"))
    return {"pass":not missing and not exact_patch and evaluable and rollback,"missing":missing,"exact_prompt_patch":exact_patch}

def promotion_gate(p,metrics):
    reasons=[]
    q=proposal_quality(p)
    if not q["pass"]:reasons.append("proposal_quality")
    if not metrics.get("pattern_gate_pass"):reasons.append("pattern_gate")
    if not metrics.get("root_cause_documented"):reasons.append("root_cause")
    suites=metrics.get("deterministic_suites",{})
    if not suites or any(v<100 for v in suites.values()):reasons.append("deterministic_regression")
    if metrics.get("critical_regressions",0)>0:reasons.append("critical_regression")
    if not metrics.get("target_failure_improved"):reasons.append("target_not_improved")
    # If live was required but missing, candidate can be offline validated, not live proven.
    live_required=bool(metrics.get("live_required"))
    live=metrics.get("live_metrics")
    live_ok=True
    if live_required:
        if not live:
            live_ok=False
        else:
            live_ok = (
                live.get("mean_quality_delta",0)>=3 and
                live.get("thinking_os_win_rate",0)>=55 and
                live.get("baseline_win_rate",100)<=25 and
                live.get("max_domain_regression",999)<=3
            )
            if not live_ok:reasons.append("live_quality_gate")
    if reasons:
        status="rejected"
    elif live_required and not live:
        status="offline_validated"
    else:
        status="ready_for_review"
    return {"status":status,"pass":status=="ready_for_review","reasons":reasons,"live_proven":bool(live_required and live_ok and live)}

def main():
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest="cmd",required=True)
    v=sp.add_parser("validate");v.add_argument("record")
    d=sp.add_parser("patterns");d.add_argument("record")
    q=sp.add_parser("proposal-check");q.add_argument("proposal")
    g=sp.add_parser("promotion-gate");g.add_argument("proposal");g.add_argument("metrics")
    args=ap.parse_args()
    if args.cmd=="validate":
        e=validate_record(load(args.record));print(json.dumps({"valid":not e,"errors":e},indent=2))
        if e:raise SystemExit(1)
    elif args.cmd=="patterns":
        print(json.dumps(detect_patterns(load(args.record)),ensure_ascii=False,indent=2))
    elif args.cmd=="proposal-check":
        print(json.dumps(proposal_quality(load(args.proposal)),ensure_ascii=False,indent=2))
    else:
        print(json.dumps(promotion_gate(load(args.proposal),load(args.metrics)),ensure_ascii=False,indent=2))

if __name__=="__main__":main()
