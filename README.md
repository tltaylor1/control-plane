# control-plane

![control-plane: the shared platform grid behind the applications](images/control-plane-banner.png)

**Documentation site**, this document with side navigation and search:
<https://tltaylor1.github.io/control-plane/>.

control-plane is the platform that manifest-identity and the
applications after it run on: an AWS estate defined as code, with
every security choice explained beside the code that makes it. It is
built in public by one person with an AI coding agent under
[build-doctrine](https://github.com/tltaylor1/build-doctrine), and it
is the part of the program still to build.

It will hold:

- The organization and its accounts as code: a near-empty management
  account, organizational units, service control policies, budgets and
  alarms before any resource exists.
- Two stacks side by side. A persistent foundation, the accounts,
  state, and identity, and an ephemeral workload, the network, the
  cluster, and the application, torn down and rebuilt daily so
  recovery is routine rather than rehearsed.
- The network and why it is shaped that way: private subnets, a
  database no route reaches from outside, egress controlled.
- Identity without stored keys: people through short-lived sessions,
  pipelines through federation into scoped roles, workloads through
  the cluster's own identity.
- The image promoted by digest and its attestation checked before it
  runs.
- The cloud's own recorders switched on: an organization trail, threat
  detection, a configuration baseline with drift alarms, the access
  analyzer reading every role.
- Recovery drilled on a schedule, with the date each drill last ran.
- Write access to the estate last, because it is earned by everything
  before it.

## Where it stands

No code exists yet. The plan for the first phase is written and
published before the work starts, so a change of plan is a recorded
decision and not a quiet edit.

The phases of the platform:

3. The cloud enclave as code: the organization, the accounts, the
   foundation stack.
4. Managed Kubernetes: the image promoted into the enclave by digest.
5. The security-gated pipeline, proven by planting a flaw.
6. Runtime detection and response, with the first-hour procedure
   written and exercised once.
7. Human-triggered remediation, last: a scoped action credential,
   step-up authentication, every action shown as a diff before it
   happens and verified against the provider afterwards.

Phases 0 to 2, design, the application, and local Kubernetes, were
manifest-identity's and are complete; the arc below shows all eight.

![The eight phases as a timeline, with the current position marked](diagrams/phase-journey-sketch.svg)

## The documents

Each is kept here because it is about the platform, and each carries
the date it was last checked.

- [The Phase 3 plan](PHASE-3.md): the shape of the estate, the
  subphases, and what done means for each.
- [Monitoring](MONITORING.md): what is watched at each layer, what
  signal it gives, and who hears it.
- [Recovery](BCDR.md): what is rebuilt from code, what real state is
  backed up, and when each drill last ran.
- [Decisions](DECISIONS.md): what was chosen, what was rejected, and
  why, including why this repository is the platform.

## The posture

Terraform as the tool. State in versioned object storage with native
locking. No account identifier in a shipped module, so the modules
are generic and the estate's own values live apart. No stored cloud
credential anywhere. A plan is a claim about intent, so the cloud's
own configuration record is the independent reviewer of what exists.
The gates every repository shares, what a platform repository adds,
and this posture in full are in build-doctrine's enforcement record,
under [Every repository's pipeline](https://tltaylor1.github.io/build-doctrine/02-enforcement/#every-repositorys-pipeline).

The program as a whole, its rulebook, its application, and this
platform, is mapped at <https://tltaylor1.github.io>.
