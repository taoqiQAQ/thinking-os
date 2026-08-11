#!/usr/bin/env python3
from pathlib import Path
import argparse, copy, datetime, json

ALLOWED_STATUS={"exploring","testing","committed","paused","pivoting","stopped","closed"}
ASSUMPTION_STATUS={"untested","supported","weakened","falsified","superseded"}
QUALITY={"verified","probable","anecdotal","speculative"}
DIRECTION={"supports","challenges","neutral","mixed"}
TRANSITIONS={
 "exploring":{"testing","committed","paused","stopped","closed"},
 "testing":{"exploring","committed","paused","pivoting","stopped","closed"},
 "committed":{"testing","paused","pivoting","stopped","closed"},
 "paused":{"exploring","testing","committed","pivoting","stopped","closed"},
 "pivoting":{"testing","committed","paused","stopped","closed"},
 "stopped":{"closed"},"closed":set()
}
def now(): return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def save(p,s): Path(p).write_text(json.dumps(s,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def idset(s,f,k): return {x.get(k) for x in s.get(f,[])}

def validate(s):
    e=[]; req=["schema_version","decision_id","decision_question","objective","status","created_at","updated_at",
    "current_recommendation","confidence","probability_estimates","assumptions","evidence","kill_criteria","scale_criteria","decision_journal","reviews","outcomes"]
    for k in req:
        if k not in s:e.append("missing:"+k)
    if s.get("schema_version")!="1.5":e.append("schema_version")
    if s.get("status") not in ALLOWED_STATUS:e.append("status")
    c=s.get("confidence")
    if not isinstance(c,(int,float)) or not 0<=c<=1:e.append("confidence")
    for f,k in [("assumptions","assumption_id"),("evidence","evidence_id"),("kill_criteria","criterion_id"),
                ("scale_criteria","criterion_id"),("decision_journal","journal_id"),("reviews","review_id"),("outcomes","outcome_id")]:
        vals=[x.get(k) for x in s.get(f,[])]
        if None in vals:e.append(f"{f}:missing-id")
        if len(vals)!=len(set(vals)):e.append(f"{f}:duplicate-id")
    aids=idset(s,"assumptions","assumption_id"); eids=idset(s,"evidence","evidence_id")
    for a in s.get("assumptions",[]):
        if a.get("status") not in ASSUMPTION_STATUS:e.append(f"{a.get('assumption_id')}:status")
        if not 1<=int(a.get("criticality",0))<=5:e.append(f"{a.get('assumption_id')}:criticality")
        if not 1<=int(a.get("uncertainty",0))<=5:e.append(f"{a.get('assumption_id')}:uncertainty")
        for x in a.get("evidence_refs",[]):
            if x not in eids:e.append(f"{a.get('assumption_id')}:unknown-evidence:{x}")
    for x in s.get("evidence",[]):
        if x.get("quality") not in QUALITY:e.append(f"{x.get('evidence_id')}:quality")
        if x.get("direction") not in DIRECTION:e.append(f"{x.get('evidence_id')}:direction")
        if not 1<=int(x.get("relevance",0))<=5:e.append(f"{x.get('evidence_id')}:relevance")
        for aid in x.get("assumption_refs",[]):
            if aid not in aids:e.append(f"{x.get('evidence_id')}:unknown-assumption:{aid}")
    for p in s.get("probability_estimates",[]):
        v=p.get("probability")
        if not isinstance(v,(int,float)) or not 0<=v<=1:e.append(f"{p.get('hypothesis_id')}:probability")
    return e

def journal(s,event_type,summary,refs=None,before=None,after=None,ts=None):
    existing=idset(s,"decision_journal","journal_id"); n=1
    while f"J{n}" in existing:n+=1
    s["decision_journal"].append({"journal_id":f"J{n}","timestamp":ts or now(),"event_type":event_type,
    "summary":summary,"evidence_refs":refs or [],"before":before,"after":after})

def add_evidence(s,e):
    if e["evidence_id"] in idset(s,"evidence","evidence_id"):raise ValueError("duplicate evidence_id")
    for aid in e.get("assumption_refs",[]):
        if aid not in idset(s,"assumptions","assumption_id"):raise ValueError("unknown assumption")
    if e["quality"] not in QUALITY or e["direction"] not in DIRECTION:raise ValueError("invalid evidence classification")
    if not 1<=int(e["relevance"])<=5:raise ValueError("invalid relevance")
    item={k:e.get(k) for k in ["evidence_id","observed_at","source","summary","quality","direction","relevance","assumption_refs","expires_at"]}
    item["observed_at"]=item["observed_at"] or now();item["assumption_refs"]=item["assumption_refs"] or []
    s["evidence"].append(item)
    for a in s["assumptions"]:
        if a["assumption_id"] in item["assumption_refs"]:
            if item["evidence_id"] not in a["evidence_refs"]:a["evidence_refs"].append(item["evidence_id"])
            a["updated_at"]=item["observed_at"]
    s["updated_at"]=item["observed_at"];journal(s,"manual_note","Evidence added: "+item["evidence_id"],[item["evidence_id"]],ts=item["observed_at"])

def update_assumption(s,e):
    a=next((x for x in s["assumptions"] if x["assumption_id"]==e["assumption_id"]),None)
    if not a:raise ValueError("unknown assumption")
    new=e["status"]
    if new not in ASSUMPTION_STATUS:raise ValueError("invalid assumption status")
    if a["status"]=="falsified" and new=="supported":raise ValueError("falsified cannot silently return supported")
    refs=e.get("evidence_refs",[])
    for x in refs:
        if x not in idset(s,"evidence","evidence_id"):raise ValueError("unknown evidence")
    old=a["status"];ts=e.get("timestamp",now());a["status"]=new;a["updated_at"]=ts
    a["evidence_refs"]=list(dict.fromkeys(a.get("evidence_refs",[])+refs));s["updated_at"]=ts
    journal(s,"assumption_update",e.get("reason",f"{old}->{new}"),refs,{"status":old},{"status":new},ts)

def update_belief(s,e):
    p=next((x for x in s["probability_estimates"] if x["hypothesis_id"]==e["hypothesis_id"]),None)
    if not p:raise ValueError("unknown hypothesis")
    refs=e.get("evidence_refs",[])
    if not refs:raise ValueError("belief update requires evidence_refs")
    for x in refs:
        if x not in idset(s,"evidence","evidence_id"):raise ValueError("unknown evidence")
    if not e.get("reason"):raise ValueError("belief update requires reason")
    new=float(e["probability"])
    if not 0<=new<=1:raise ValueError("probability out of range")
    old=float(p["probability"]);ts=e.get("timestamp",now());p["probability"]=new;p["updated_at"]=ts
    after={"hypothesis_id":e["hypothesis_id"],"probability":new}
    if "confidence" in e:
        conf=float(e["confidence"])
        if not 0<=conf<=1:raise ValueError("confidence out of range")
        s["confidence"]=conf;after["confidence"]=conf
    s["updated_at"]=ts;journal(s,"belief_update",e["reason"],refs,{"hypothesis_id":e["hypothesis_id"],"probability":old},after,ts)

def update_recommendation(s,e):
    if not e.get("reason"):raise ValueError("recommendation update requires reason")
    refs=e.get("evidence_refs",[])
    for x in refs:
        if x not in idset(s,"evidence","evidence_id"):raise ValueError("unknown evidence")
    old=s["current_recommendation"];ts=e.get("timestamp",now());s["current_recommendation"]=e["recommendation"];s["updated_at"]=ts
    journal(s,"recommendation_update",e["reason"],refs,{"recommendation":old},{"recommendation":e["recommendation"]},ts)

def update_status(s,e):
    old=s["status"];new=e["status"]
    if new not in TRANSITIONS.get(old,set()):raise ValueError(f"invalid status transition:{old}->{new}")
    ts=e.get("timestamp",now());s["status"]=new;s["updated_at"]=ts
    journal(s,"status_update",e.get("reason",f"{old}->{new}"),e.get("evidence_refs",[]),{"status":old},{"status":new},ts)

def trigger_criterion(s,e):
    f="kill_criteria" if e["criterion_type"]=="kill" else "scale_criteria"
    c=next((x for x in s[f] if x["criterion_id"]==e["criterion_id"]),None)
    if not c:raise ValueError("unknown criterion")
    if c["status"]=="superseded":raise ValueError("superseded criterion")
    refs=e.get("evidence_refs",[])
    for x in refs:
        if x not in idset(s,"evidence","evidence_id"):raise ValueError("unknown evidence")
    old=c["status"];c["status"]="triggered";c["evidence_refs"]=list(dict.fromkeys(c.get("evidence_refs",[])+refs))
    ts=e.get("timestamp",now());s["updated_at"]=ts
    journal(s,"criterion_update",f"{e['criterion_type']} criterion {e['criterion_id']} triggered",refs,{"status":old},{"status":"triggered"},ts)

def add_outcome(s,e):
    if e["outcome_id"] in idset(s,"outcomes","outcome_id"):raise ValueError("duplicate outcome")
    ts=e.get("timestamp",now());s["outcomes"].append({"outcome_id":e["outcome_id"],"timestamp":ts,"summary":e["summary"],
    "process_quality":e.get("process_quality"),"outcome_quality":e.get("outcome_quality")});s["updated_at"]=ts
    journal(s,"manual_note","Outcome recorded: "+e["outcome_id"],[],ts=ts)

HANDLERS={"add_evidence":add_evidence,"update_assumption":update_assumption,"update_belief":update_belief,
"update_recommendation":update_recommendation,"update_status":update_status,"trigger_criterion":trigger_criterion,"add_outcome":add_outcome}

def apply_event(s,e):
    out=copy.deepcopy(s);t=e.get("type")
    if t not in HANDLERS:raise ValueError("unknown event type")
    HANDLERS[t](out,e);errs=validate(out)
    if errs:raise ValueError(";".join(errs))
    return out

def summary(s):
    aa=sorted(s["assumptions"],key=lambda a:a["criticality"]*a["uncertainty"],reverse=True)
    return {"decision_id":s["decision_id"],"status":s["status"],"recommendation":s["current_recommendation"],
    "confidence":s["confidence"],"probabilities":{p["hypothesis_id"]:p["probability"] for p in s["probability_estimates"]},
    "top_assumptions":[{"id":a["assumption_id"],"status":a["status"],"priority":a["criticality"]*a["uncertainty"]} for a in aa[:3]],
    "triggered_kill":[c["criterion_id"] for c in s["kill_criteria"] if c["status"]=="triggered"],
    "triggered_scale":[c["criterion_id"] for c in s["scale_criteria"] if c["status"]=="triggered"],
    "evidence_count":len(s["evidence"]),"journal_entries":len(s["decision_journal"])}

def main():
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest="cmd",required=True)
    v=sp.add_parser("validate");v.add_argument("state")
    a=sp.add_parser("apply");a.add_argument("state");a.add_argument("event");a.add_argument("--out",required=True)
    q=sp.add_parser("summary");q.add_argument("state")
    x=ap.parse_args()
    if x.cmd=="validate":
        er=validate(load(x.state));print(json.dumps({"valid":not er,"errors":er},ensure_ascii=False,indent=2))
        if er:raise SystemExit(1)
    elif x.cmd=="apply":
        s=apply_event(load(x.state),load(x.event));save(x.out,s);print(x.out)
    else:print(json.dumps(summary(load(x.state)),ensure_ascii=False,indent=2))
if __name__=="__main__":main()
