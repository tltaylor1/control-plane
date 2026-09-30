# control-plane

One person's public record of building a security engineering
program with an AI agent doing the typing and a human deciding
everything.

It exists to show, with evidence rather than claims, that agent-built
software can be held to a professional standard: every decision
recorded with what was rejected, every control proven by a test,
every release attested, and every agent mistake written down with
what caught it.

What is in it:

- **manifest-identity**: two records about every identity in a cloud
  estate, what it holds and what a named person said it may hold, and
  the difference between them. Six providers read natively, any other
  through a table; review campaigns driven by the calendar, the delta,
  or expiry. more than 400 tests, 82 recorded decisions, five outside ratings.
- **build-doctrine**: the rulebook the program builds under, and the
  commands that score any repository against it.
- **secure-expense-mvp**: a small finished application, hardened and
  mutation-tested, kept as the reference.
- **The program documents**: what is monitored, how recovery works,
  how every repository is gated, and the next phase's plan.

The rendered site is this repository, served at
https://tltaylor1.github.io.

## The parts

| Repository | What it is, and what it proves |
|---|---|
| [manifest-identity](https://github.com/manifest-identity/manifest-identity) | Governance for the identities nobody owns: what each identity holds, read from six providers' own exports, beside what a named person said it may hold, and every difference put in front of the person who can answer it. The program's flagship: building in motion, with the decision record growing under load |
| [secure-expense-mvp](https://github.com/tltaylor1/secure-expense-mvp) | A small expense tool, finished and hardened: every request-path gate tied to the failure it prevents, mutation-tested, complete on purpose |
| [build-doctrine](https://github.com/tltaylor1/build-doctrine) | The doctrine: standards where every rule records the incident that produced it, the enforcement mapping, and the promotion path from human check to automated gate |
| aws-platform | Arrives with Phase 3: generic Terraform modules for an organization, its baseline, account vending, and keyless deploy federation |

## The program documents

The things one repository cannot answer for, kept here:

- **[The plan](PHASE-3.md)** for the current phase, written and
  published before the work starts, so a change of plan is a
  recorded decision and not a quiet edit.
- **[Monitoring](MONITORING.md)**: what is watched at each layer,
  what signal it gives, and who hears it. A layer with nothing
  watching it says so.
- **[Recovery](BCDR.md)**: what can be rebuilt from code and what is
  real state that must be backed up. Each recovery drill carries the
  date it last ran and goes stale on a schedule.
- **[Pipelines](PIPELINES.md)**: how every repository blocks a bad
  change, and how the tools that do the blocking are themselves
  verified before they run.

## The method

- Design first. The plan is public before the first line of code.
- Every change is a pull request: the agent proposes under its own
  identity, the checks must pass, a human must approve, and the
  merge is the receipt.
- Every figure in a document is checked against the running system,
  or a test fails.
- Every mistake becomes a rule, and the second time a fix is done by
  hand it becomes automation.
- What was left out on purpose is written down beside what was built.

## The arc

![The eight phases as a timeline, with the current position marked](diagrams/phase-journey-sketch.svg)

Eight phases, counted from zero so the numbers match the ones the
repositories use: Phase 0, design; 1, the application; 2, local
Kubernetes; 3, the cloud enclave as code; 4, managed Kubernetes; 5,
the security-gated pipeline; 6, runtime detection; 7, human-triggered
remediation, last, because write access to anyone's cloud account is
trust that must be earned by everything before it. Phases 0 through 2
are complete. Phase 1 built the observed half of manifest-identity in
twelve review-gated subphases, tagged v0.2.0 with Phase 2 and carrying
verifiable build provenance, and then the authorized half in fourteen
more, merged after that tag. The Phase 3 plan is written in
[PHASE-3.md](PHASE-3.md); no Phase 3 code exists yet.
