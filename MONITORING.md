# Monitoring, the platform view

What is watched at each layer, what signal it produces, and who hears
it. This is the frame; each phase of the build fills its layer, and a
layer that is not yet filled says so rather than implying coverage.

| Layer | What is watched | Signal | Who hears it | State |
|---|---|---|---|---|
| Application | Every request (structured logs, allowlisted fields); every governance action (the audit table); liveness and readiness on the database round trip | Log lines; audit rows; probe failures restart or de-route the pod | The operator reading the audit view; the orchestrator acting on probes | Present |
| Detection queries | Failed sign-ins per account, denied access attempts, disposition rates | Queries exist over the audit table | A person running them; alerting arrives with the runtime phase | Frame only, fills at Phase 6 |
| Cluster | Rollout status, pod restarts, admission refusals | Orchestrator events | A person running the drills; scraped metrics arrive with the runtime phase | Partial |
| Cloud account | Root use, console sign-ins, all control-plane activity (organization trail); posture findings (the built-in reviewers); spend (budget alarms at three thresholds) | Trail events; findings; billing alarms to the inbox | The human, by email, before anything else exists | Arrives at Phase 3 |
| Pipeline | Every gate on every pull request; the weekly scheduled run for what changes while code does not; the externally published posture score | Red checks block merges; scheduled failures land on the main branch view | The human, on the pull request or the repository page | Present |

The principle carried from the application outward: a signal nobody
hears is storage, not monitoring, so every row names its listener, and
the rows whose listener is "a person who remembers to look" are the
ones the runtime phase exists to fix.
