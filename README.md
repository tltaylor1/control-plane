# control-plane

![control-plane: the shared platform grid behind the applications](images/control-plane-banner.png)

control-plane is a security engineering program that one person is
building in public with an AI coding agent. The agent writes the code
and the documents; the person reviews and approves every change; every
decision and every mistake is recorded. It has three parts.

build-doctrine is the rulebook for all the code. It is the standards
for letting an AI agent write code that a person is responsible for,
and it provides the tools that check any repository against them.

It carries:

- Rules where each one names the problem behind it and the check that
  catches it.
- A scorer that grades any repository from 0 to 5 on each rule.
- A vetting tool that examines a dependency before it is adopted.
- A project template with the checks already switched on.
- Coverage of seven frameworks: OWASP Top 10, OWASP API Security Top
  10, OWASP Top 10 for LLM Applications, STRIDE, NIST SSDF, OWASP ASVS,
  and SLSA. Eighty items mapped to the rules, gaps listed.

manifest-identity is the application built under those rules. It
keeps two records about every identity in a cloud estate, what access
it holds and what access a named person authorized, and it shows
every difference between them.

It has:

- Seven providers read from their own export files: AWS, GitHub,
  Kubernetes, Google Cloud, Azure and Entra, Okta, Active Directory.
  Any other provider through a table.
- Review campaigns that put each difference in front of the person
  responsible for it, one decision at a time.
- Twenty findings, each explaining itself: unused identities, keys past
  their age, administrators by capability, trusts open to the world.
- A read-only API and a change feed, so other systems follow the
  decisions.
- Figures: more than 400 tests, 84 recorded decisions, 34 controls proven by
  mutation, five outside ratings, a release verifiable with one
  command.

The cloud deployment is the part still to build, phases 3 to 7. It is
the application run in AWS the way the rulebook says.

It will have:

- An AWS organization defined as code.
- One account that persists; the workloads inside it torn down and
  rebuilt daily, so recovery is routine.
- Deploys without stored credentials; the image promoted by digest.
- The pipeline tested by planting a flaw; the cloud's own monitoring
  switched on.
- The ability to change a cloud account comes last, earned by
  everything before it. Each phase's plan is published before the work.

secure-expense-mvp is a small application built before the program as
a learning exercise, kept as a reference.

This repository is the program's home. Its documents render as a site
with side navigation and search at
<https://tltaylor1.github.io/control-plane/>, generated from these files
at build time; the account's own page is at <https://tltaylor1.github.io>.

## The parts

The program is four repositories. Each is public, and each is scored
against the rulebook in its own pipeline.

They are:

- [manifest-identity](https://github.com/manifest-identity/manifest-identity):
  the application.
- [build-doctrine](https://github.com/tltaylor1/build-doctrine): the
  rulebook, the scorer, the vetting tool, and the template.
- aws-platform: the cloud deployment, arriving with Phase 3 as
  reusable Terraform modules for an organization, its baseline,
  account vending, and keyless deploys.
- [secure-expense-mvp](https://github.com/tltaylor1/secure-expense-mvp):
  the learning exercise from before the program, kept as a reference.

## The program documents

Some things no single repository can answer for. They are kept here,
and each carries the date it was last checked, so it goes stale on a
schedule rather than quietly.

They are:

- [The plan](PHASE-3.md) for the current phase, published before the
  work starts, so a change of plan is a recorded decision.
- [Monitoring](MONITORING.md): what is watched at each layer, what
  signal it gives, and who hears it.
- [Recovery](BCDR.md): what is rebuilt from code and what real state
  is backed up, with the date each drill last ran.
- [Pipelines](PIPELINES.md): how every repository blocks a bad change,
  and how the blocking tools are verified before they run.

## The method

Every change takes the same path, whichever repository it is in. The
agent proposes, the checks run, and a person approves.

The rules of the path:

- Design first. The plan is public before the first line of code.
- Every change is a pull request under the agent's own identity. The
  checks must pass, a person must approve, and the merge is the record.
- Every figure in a document is checked against the running system, or
  a test fails.
- Every mistake becomes a rule, and the second time a fix is done by
  hand it becomes automation.
- What was left out on purpose is written down beside what was built.

## The arc

![The eight phases as a timeline, with the current position marked](diagrams/phase-journey-sketch.svg)

The program runs in eight phases, counted from zero to match the
repositories. Phases 0 to 2 are complete. The Phase 3 plan is written
in [PHASE-3.md](PHASE-3.md), and no Phase 3 code exists yet.

The phases:

0. Design, before any code.
1. The application: the observed half in twelve review-gated
   subphases, then the authorized half in fourteen more.
2. Local Kubernetes: admission, network policy, identity.
3. The cloud enclave as code.
4. Managed Kubernetes.
5. The security-gated pipeline, proven by a planted flaw.
6. Runtime detection and response.
7. Human-triggered remediation, last, because write access is earned.
