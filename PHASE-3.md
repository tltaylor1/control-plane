# Phase 3: the cloud enclave as code

The third phase moves manifest-identity onto a real cloud account, as code,
with the account's own posture held to the same standard as the code's.
This is the public plan, fixed before the work; discoveries during the
build become recorded decisions, not silent amendments.

## The shape

- An AWS Organization: a near-empty management account as billing and
  policy root, hardware-key credentials, no root access keys, root use
  alarmed; organizational units for workloads and sandbox; two service
  control policies to start, denying regions outside the home pair and
  denying root-user actions.
- Accounts persist, stacks are ephemeral: one sandbox member account
  stands, and the enclave inside it is destroyed and reapplied daily
  by script, so recovery is rehearsed by routine. An account-vending
  module exists from the start, because applications get vended
  accounts as the standing pattern.
- Budgets and alarms exist before any resource does.
- A generic platform repository holds the modules (organization,
  baseline, vending, network, deploy federation) with no application's
  name in them; applications consume versioned modules and keep their
  own glue.
- Terraform as the tool, for its adoption; state in versioned S3 with
  native locking; no stored cloud credential anywhere, humans through
  short-lived sessions and pipelines through OIDC federation into
  scoped roles.
- Control Tower declined deliberately: toil chosen over spend, because
  its per-account plumbing bills continuously while doing the
  instructive work invisibly, and the decision entry names what it
  would have provided so adopting it later stays an informed move.
- The cloud's own reviewers enabled as code: Config with a
  conformance baseline as the independent record of what exists,
  Security Hub's foundational standard, the organization access
  analyzer, GuardDuty on the sandbox, and drift detection on a weekly
  schedule, because a plan is a claim and the account is the fact.

## The subphases

1. **Baseline and organization.** The platform baseline document
   written first, every row checked, attested, or accepted; then the
   organization, identity, budgets, guardrails, and the sandbox
   account; a threat model revision for the new surfaces.
2. **The platform repository.** Born fully governed; the foundation
   applied from a short-lived session: state backend, deploy
   federation, the organization trail into a locked bucket, the
   registry, and the reviewers above.
3. **The enclave, ephemeral.** The network module without standing
   cost traps, the vending module proven by vending one account, the
   daily destroy-apply drill scripted and timed, and the pipeline
   pushing the application's image to the registry through
   federation, with no key existing anywhere to steal.
4. **The trail meets the application.** The organization trail
   queryable; creator attribution enters the application's design
   file-first; the sample account generator gains a deterministic
   scale mode, and the inventory gains the pagination that thousands
   of identities require.
5. **Proof.** Rebuild from the documents alone, the first bill against
   the budget, baseline attestations current, findings triaged to
   fixed or accepted, diagrams and documents updated.

## What this phase deliberately does not do

No production traffic, no real identities, no live provider connection
from the application yet, and no managed Kubernetes, which is the next
phase's move of a workload the local cluster already proved.
