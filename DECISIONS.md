# Decisions

What was chosen, what was rejected, and why, for the program
repository itself. Each repository in the program keeps its own
record; this one governs the umbrella.

## D-001: The program is named control-plane

The name states the subject: the human is the control plane, directing
the workloads without doing the work packet by packet, through
architecture, standards, and gates. The rejected candidates and their
reasons: names built on the evidence the method produces (paper-trail,
receipts, show-your-work) described the symptoms rather than the
system; governor and the-score carried the control idea but needed
explaining; plane-control inverted a term of art and would read as
unfamiliarity to exactly the audience that knows the term. Taking the
canonical term straight and letting the twist live in the tagline won.

## D-002: Identity is scoped to what it works on

The signing key and the installed-app identity that serve the
application repository serve only it. This repository and future
program repositories get their own: a control-plane signing key and a
control-plane agent app, created under the same recorded pattern as
every identity here, need, request, approval. One boundary stated
plainly: this repository's first commit predates this decision and is
signed by the application repository's key; it stays as it is, because
rewriting published history to repair a label would destroy the record
the signatures exist to protect.

## D-003: This repository is the platform, and the program has no repository

The program's page lived here for a month and repeated the two
repositories it pointed at, and its plan sections were amended in
those repositories and not here, because nothing checked them. A
document that is only evidence of a plan goes stale the moment the
plan moves.

What this repository held that nothing else did was about the
platform: the Phase 3 plan, what is monitored, how recovery is
drilled. So the repository becomes the platform, an AWS estate as
code with its choices explained, which is what the name and the
banner already said. The plan stays where the code will be, which is
the plan-before-code rule applied in place. The map of the program
moves to the account's own page, and the pipelines overview moves to
build-doctrine's enforcement record, where it is doctrine and where
its checks hold it.

Rejected: archiving this repository and creating another for the
platform, which would leave a copy of every document behind with a
banner on it; deleting it, which would lose the record of its
eighteen reviewed changes for nothing; and a second, private
repository for the estate's own values from the start, which waits
for the first value that must not be public.

The cost is a repository whose history opens with a program page it
no longer is, which this entry explains.
