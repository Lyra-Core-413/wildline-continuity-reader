# Wildline Continuity Reader

**AI should remember your story, not write your future.**

**CONTINUITY WITHOUT CAPTIVITY**

> Know me well enough to recognize me. Stay curious enough to let me change.

Wildline is an emerging AI continuity architecture. It explores how an AI can preserve *what changed because of an experience*, not just what a transcript, summary, or memory once said.

This repository contains a **small, inspectable MIT-licensed demonstration of the continuity reader**, not the complete Wildline product. Its offline examples are **fictional**. No Bee account data or private personal Core history is included; the founder-approved story below explains why it exists.

## Why I began

I bought an Amazon Bee because I thought it looked cool.

Seriously.

At work, I was buried in meetings, corridor decisions, emails, responsibilities and lists of things to keep track of. I connected Bee context to ChatGPT and developed a Daily Command Center that became genuinely helpful at sorting commitments from noise.

Then, from one day to the next, too much of our *working understanding* needed to be rebuilt. We could retain a fact while losing why we'd challenged it, what we'd corrected, or what remained unresolved.

That led to a personal continuity system called **Lyra Core**. It developed around my own life and work. The next question was harder: **How do we make that capability available to someone else without giving them my history?**

Wildline is the effort to extract those reusable mechanisms. **Portable constitution. Non-portable biography.**

[Read the fuller founder story](docs/PROJECT-STORY.md).

**Historical export scope:** The earlier private founder presentation was excluded from the historical source export. The current public documentation includes an approved, high-level Wildline origin and project story. Private Lyra Core history, personal Bee content and sensitive founder evidence remain excluded.

## The idea in one minute

A system observes that you committed to a task. Later, you delegate the task. Later still, it is completed.

Recording each statement isn't enough. A useful continuity system needs to preserve the evidence, know what changed, recognize what still applies, and avoid silently granting itself permission to act.

Wildline is designed around five distinctions:

| Question | What Wildline aims to preserve |
| --- | --- |
| **What happened?** | Source evidence and provenance |
| **What changed?** | Correction, supersession and revision history |
| **What remains uncertain?** | Gaps, competing interpretations and unresolved status |
| **Who decides?** | User authority and explicit permission boundaries |
| **What carries forward?** | Relevant, supported context for a later interaction |

Our working method also follows a rhythm: **411 Recover → 413 Challenge → 412 Reconstruct.** It is a reasoning and development method, not a claim that every experimental Core capability ships in this small release.

[Architecture and boundaries](docs/ARCHITECTURE-AND-BOUNDARIES.md)

## VERIFIED — try the fictional offline demonstration

This is **public RC3 MIT**, a separately versioned, 25-file release candidate derived from RC2. Executable code, tests and fictional fixtures are unchanged. It is prepared locally and has not been published.

Use Windows x64 and separately installed `python` on PATH, tested with CPython 3.14.7. No pip packages, Core files or Bee account are needed. From a complete clean extraction of this RC3 package:

```powershell
.\RUN-JUDGE.cmd
```

The actual H5 reader compares fictional A/B observations and displays its recovered answer in a separate process with history, provenance, uncertainty and authority NONE. It makes no Bee call.

[Build and tests](docs/BUILD-AND-TEST.md) · [Judge guide](docs/DEMO-AND-VERIFICATION.md)

## Evidence boundaries

**VERIFIED — what the evidence supports**

The **public-source RC1** passed 48 clean-extraction tests with fictional data, according to its retained verification report. **Separately**, the private Wildline bridge passed 107 tests with fictional/mock inputs and subsequently completed one founder-authorized real Bee Fact read followed by recovery of its selected content in a distinct process, with an independently checked private receipt.

A third, separate historical demonstration shows authorized recorded stages of a Bee Fact's correction, partial reconfirmation and deletion. That is an evidence replay, not a newly observed live change.

**EXPERIMENTAL:** Advanced Reflection and Between remain separate Lab work, absent from this release.

**Not claimed:** automatic Bee synchronization; verified physical-microphone attribution; change/no-change detection from a single observation; autonomous action; portable production deployment; independent second-PC verification; or completion of the advanced Reflection and Between research.

The real Bee runtime adapter, private receipts and source content **are not included in this public-source candidate**. See [Evidence boundaries](docs/EVIDENCE-BOUNDARIES.md).

## FUTURE VISION — where Wildline could go

The longer-term goal is an empty, person-governed continuity core that can grow around *someone else's* experiences and permissions, not an AI trained to imitate mine.

That opens questions for leaders, teachers, caregivers and people navigating change. Caregiving and peer hospice support are possible research directions. This is a **future exploration**, not a deployed care system or current clinical capability.

It also raises a bigger question: can an AI become more useful through a continuing collaboration **without becoming increasingly certain it has defined the person**?

Our commitment is to preserve wonder, disagreement, corrections and the freedom to surprise ourselves. [Read the research directions](docs/ROADMAP-AND-VISION.md).

## Status and safeguards

- **Status:** MIT-licensed public RC3 release candidate, prepared locally and unpublished; not a production application.
- **Privacy:** No private Bee transcripts, account identifiers, credentials, live receipts, or Lyra Core databases should be published.
- **License:** [MIT](LICENSE), **Copyright (c) 2026 Eric Staiger**, for authorized project-owned source and documentation. External software and any independently owned materials retain their applicable licenses; no license is granted to private Bee data or Lyra Core history.
- **Testing:** The prepared offline candidate passed tests on the development Windows PC. It has **not been independently tested on a second computer**. The founder has deferred that testing for the hackathon; another computer's compatibility remains unverified. This does not change the scope or validity of the existing same-computer technical proof.

Use and redistribution of the licensed project-owned materials are permitted under the complete [MIT License](LICENSE). GitHub publication still requires Eric's separate authorization. See [license scope and external dependencies](LICENSE-REVIEW.md).

**Preserve the line. Keep it wild.**

**Bee is an evidence source, not automatic truth or permission.**

**Lyra Core: personal reference; Wildline: portable architecture; Wildline Lab: isolated testing.**

**Portable constitution. Non-portable biography.**

**411 Recover → 413 Challenge → 412 Reconstruct**

## Release integrity and publication

This RC3 licensing derivative has its own 25-file inventory, RELEASE-MANIFEST.json and RELEASE-MANIFEST.sha256. The original RC2 and its seals remain unchanged. Any later package change requires a separately versioned derivative and refreshed verification. Local hashes prove consistency, not publisher authentication.

Earlier documentation alignment performed no software tests or Bee calls. This licensing task reruns the unchanged public 48-test suite from clean extraction and records its result in a separate verification receipt. No Bee access is part of this public reader.
