# Build and test guidance

This is the **documentation-facing summary** for the published public reader and the distinct private candidates. The exact package-local manifest, test runner and setup guide take precedence when executing software. Do not treat the private development snapshot as a complete installation.

## Three distinct artifacts

| Artifact | Distribution | Default input | Environment tested | Evidence |
| --- | --- | --- | --- | --- |
| Public Continuity Reader, RC3-docs.1 | Published public source; documentation-only revision of RC3 | Fictional fixtures | Clean extraction on the development Windows PC for the unchanged RC3 software | 48 passing tests in retained RC3 licensing/publication checks |
| Private Bee-track candidate v1.1 | Prepared, not published | Fictional fixtures; separate opt-in live mode | Clean extraction on the development Windows PC | 107 passing mock/fictional tests |
| Preserved historical demonstration | Private and frozen | Authorized historical lifecycle data | Isolated Windows demonstration | Reports documented corrections, partial reconfirmation, withdrawal and fresh-process recovery |

The **separately authorized real Bee v1.1 operation** was verified after mock testing. One actual CLI read succeeded with exit 0 and no retry, and a distinct process recovered the selected information. Its private receipt is **not** a file in the public-source archive.

## Installation and execution boundaries

- Public Continuity Reader: Windows x64 and separately installed CPython 3.14.7.
- Private live mode: Official Bee CLI must be installed and authenticated separately; user enters one Fact ID and exact fresh consent required by the release's launcher.
- Run `RUN-JUDGE.cmd` only from an approved extracted package where the file exists.
- Do not run original Lyra Store/server entry points from the screened development snapshot as smoke tests. Those have omitted configurations and may mutate local state.
- No bundle has been verified on a second physical Windows machine. Document that limitation.

## Verify before distribution

1. Check the release ZIP hash against its retained manifest and verification receipt.
2. Inspect the exact file inventory, including data, binaries and nested archives, and compare it with the intended release scope.
3. Verify synthetic-only examples contain no identifying Bee account IDs or personal text.
4. Check package-local test commands actually exist and don't read or write private data.
5. Run offline tests in a clean extraction. Record their actual outputs and environment.
6. Inspect setup docs for security assumptions, special Windows permissions and missing prerequisites.
7. Resolve source-rights, third-party licenses and ownership before adding a public license grant or publishing.
8. Obtain explicit authorization for any GitHub publication or submission action.

## Provenance and authority checks

An honest result should show what was retrieved or projected, what source it refers to, what remains uncertain, whether information was superseded, and whether the system has any authority to act. The current judge reader keeps authority at **NONE** for the demonstrated observation. Avoid claiming stronger inference than the available sample supports.

## Current status and remaining limits

- MIT adoption: **ADOPTED** for authorized project-owned public-reader materials, Copyright (c) 2026 Eric Staiger. No specific conflicting file has been identified; independently owned materials retain their own rights.
- Public/open-source publication: **FOUNDER-AUTHORIZED AND PUBLISHED**. This RC3-docs.1 editorial revision is bounded to public documentation and integrity metadata.
- Different-machine compatibility: **NOT TESTED**.
- Broad source-device attestation: **UNVERIFIED**.
- Live synchronization and automated actions: **NOT CLAIMED**.

**Preserve the line. Keep it wild.**

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

## Release integrity and publication

This RC3-docs.1 editorial derivative has its own 25-file inventory, RELEASE-MANIFEST.json and RELEASE-MANIFEST.sha256. The original RC3 commit and sealed ZIP, earlier packages and private releases remain unchanged. Any later package change requires a separately versioned derivative and refreshed verification. Local hashes prove consistency, not publisher authentication.

The original RC3 licensing and publication verifications passed the unchanged public 48-test suite from clean extraction and retained their results separately. This editorial revision checks Markdown, links, privacy and exact file integrity; those historical software test results keep their original attribution. No Bee call is made and no broader relational research result is claimed.
