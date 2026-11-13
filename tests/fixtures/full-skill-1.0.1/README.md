# Previous-release fixture

The deterministic gzip files preserve exact generated reference bytes from commit `ba13976`, Plugin 1.0.1. They cover the canonical capability-map content change and commerce trailing-newline normalization during migration to 1.1.0. Their uncompressed SHA-256 values appear in `scripts/legacy-reference-hashes.json`. Tests run without Git history or network access.
