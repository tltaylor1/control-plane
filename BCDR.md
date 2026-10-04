# Business continuity and disaster recovery, the platform view

The split that organizes everything here: what is rebuildable from
code, and what is actual state. Rebuildable things have a recovery
plan of one line, apply it again; state has objectives, procedures,
and drills, and a drill that has not run recently is a hope, so every
drill row carries the date it last ran and goes stale on a schedule.

## Rebuildable from code

| Component | Recovery | Evidence |
|---|---|---|
| Every repository | Clone again; the platform holds them and local clones are working copies | Git's design |
| The compose stack | `docker compose up --build` from a fresh clone | The fresh-clone drill, run for real |
| The local cluster and its workload | Two scripts from a fresh clone | The cluster drills in the application repository |
| The cloud enclave | Reapply the stack; it is destroyed daily on purpose, so recovery is rehearsed by routine | Arrives at Phase 3 with the teardown drill |

## Actual state

| Component | Objectives | Procedure | Last drill |
|---|---|---|---|
| The application database | A daily dump bounds loss to one day; restore in minutes | Dated compressed dump, restore with the application stopped, verify by restoring into a throwaway database and comparing counts; printed in the application repository | August 19, 2026, counts matched |
| Retention of those dumps | Thirty daily, twenty-four monthly | The application repository's backup section | Same drill |
| Terraform state | Versioned bucket; loss means re-import toil, not data loss | Arrives at Phase 3 with the state backend | Not yet standing |
| The organization trail | The record of record; bucket locked against deletion | Arrives at Phase 3 | Not yet standing |
| Credentials and keys | Hardware keys with a spare enrolled; recovery codes held offline; the agent's key revocable in one click and reissuable in minutes | Provider re-enrollment | Enrollment tested August 19, 2026 |

## The enforcement

A recovery plan rots silently, which is why this document's drill
dates are attestation rows in the platform baseline framework: each
expires on its schedule, and an expired drill is a red check, not a
memory. The schedule starts honest and small: the database restore
drill quarterly, the fresh-clone drill at every phase close, the
enclave rebuild daily by design.
