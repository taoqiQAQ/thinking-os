# Belief Update Protocol

## Prior first
Record the prior before interpreting new evidence when possible.

## Evidence classification
For each item record:
- supports / challenges / neutral / mixed;
- reliability;
- relevance;
- independence;
- freshness.

Do not count repeated reports of the same upstream source as independent evidence.

## Quantitative mode
Use only when prior and likelihood information are defensible.

Prior odds = `p / (1-p)`  
Posterior odds = `prior_odds × likelihood_ratio`  
Posterior probability = `posterior_odds / (1 + posterior_odds)`

Never invent the likelihood ratio.

## Calibrated-judgment mode
Default when exact Bayesian inputs do not exist.

- weak evidence → small/no update
- strong non-decisive evidence → moderate update
- direct falsification of a critical assumption → large update
- duplicate/dependent evidence → little extra update

Every material change records:
- before
- after
- evidence refs
- reason
- what would reverse/deepen the update

## Belief is not action
Action also depends on payoff, ruin risk, reversibility, opportunity cost, and resources.

## Calibration safeguards
- More words do not imply more confidence.
- Bad outcome does not prove a reasonable decision was bad.
- Lucky outcome does not prove a poor decision was good.
- Never retroactively edit the old forecast.
- Prefer ranges when exactness is unsupported.
