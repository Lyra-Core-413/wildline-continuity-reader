# public-source — judge demonstration

## Exact public reader setup and commands

Use Windows x64 with separately installed `python` on PATH, tested with CPython 3.14.7. The intended minimum is Python 3.11, untested. No pip dependencies, bundled Python runtime, Bee client/account, API key or Core files are required. Installation may need internet; playback does not.

From a complete checkout or clean extraction of this RC3-docs.1 package:

```powershell
python --version
.\RUN-JUDGE.cmd
python -X utf8 -I -B demo\test_h5.py
python -X utf8 -I -B demo\test_release.py
python -X utf8 -I -B demo\capability_probe.py
```

There is no public `RUN-TESTS.cmd`. The retained 48-test result is 41 H5 plus 7 export tests; the capability probe is separate from that count.

```powershell
python -X utf8 -I -B demo\h5_sidecar.py --json demo
python -X utf8 -I -B demo\h5_sidecar.py historical
```

The historical command only prints a boundary notice. Fictional run/evidence files are generated in `demo/runs/` and `demo/evidence/`, which must be writable and kept out of releases. The acquisition child exits before the separate reader starts. The display is the actual recovered answer, history, provenance, uncertainty and authority NONE.

The current `RELEASE-MANIFEST.json` and `RELEASE-MANIFEST.sha256` bind this 25-file RC3-docs.1 revision. Original RC3, earlier 17-file RC1 and 24-file RC2 packages retain their own unchanged seals. The unchanged launcher still prints its original RC1 banner; the manifest identifies this documentation derivative. Local hashes are not publisher authentication.

## VERIFIED — October 11 live evidence update

One founder-authorized native CLI invocation returned exit 0, followed by a distinct acquisition/reader process pair and a recovered answer exactly matching the H5 single-observation projection. All eight private evidence files and the 28 original package files were verified; authority was NONE.

The immutable formatter prints the actual recovered answer and flushes it before completion is recorded. Terminal completion was founder-reported; no independent character-by-character screen capture was retained. Independently checked means local evidence verification, not a second physical machine or external source attestation.

The result remains source-qualified `CLAIMED_UNVERIFIED`, with device origin unverified and source-reported confirmation. Creation time is not update time. `NOT_ASSESSED_SINGLE_OBSERVATION` establishes neither change nor no-change, correction, withdrawal, writeback or synchronization. The successful one-account operation is not a general service/compatibility guarantee.

No private operation receipt, identifying Fact content/ID or captured answer is included here.

**Live v1.1 single-Fact recovery ≠ historical change replay ≠ full sync.**

Neither the fictional public demonstration nor the single-observation private Bee result proves a relational discovery advantage. The Reachable Unknown remains a research hypothesis. Prior synthetic experiments are preliminary mechanism investigations, not independent proof of superior discovery or emergent intelligence; see [Roadmap and vision](ROADMAP-AND-VISION.md).

## VERIFIED / EXPERIMENTAL / FUTURE VISION

VERIFIED means a bounded behavior supported by an attributed retained report or local operation check. EXPERIMENTAL identifies separate Lab work. FUTURE VISION identifies capabilities not delivered here. None means production readiness or independent physical-machine verification.

The real v1.1 proof is separate project evidence, absent from this ZIP. The historical correction/withdrawal and original H4 `RUN-FOUNDER.cmd` remain separate private originals, not public commands.
