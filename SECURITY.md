# Security boundary

This candidate is a trusted local offline CLI, without a server, remote user, account, or authentication surface. No external source is accepted. A caller supplying `external` mode is refused before acquisition reads and again at capture validation. No guard, provenance check, hash check, identity/scope check, or evidence immutability check is weakened for this export.

The CLI audit hook refuses socket, registry, shell/startfile, and database-opening operations. Files may be read/written only under the demonstration directory, except interpreter runtime reads. Inputs are bounded, schema checked, duplicate-key and invalid-number checked, and terminal control characters refused. Receipt publication uses exclusive creation and hash chaining; readers require the caller-supplied pair anchor and exact file inventory. Interrupted pairs are refused.

The guard is not hostile-code isolation. A local Python process owner, compromised interpreter, imported malicious code, or concurrent filesystem actor has capabilities beyond this trusted demonstration. Library use does not install the guard automatically. Use an unmodified, trusted interpreter and a fresh extraction in an ordinary user directory. Hashes establish local consistency rather than source authenticity or a publisher signature.

No authenticated adapter or external CLI is bundled. No network test contacts a service. The included capability probe tries socket construction and an out-of-scope file open, both of which must be denied before use.

There is no public security reporting endpoint yet. Public release requires a repository owner to establish one. This document does not authorize upload or modification of private evidence.
