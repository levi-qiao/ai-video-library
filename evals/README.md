# Agent Evals

`compiler-routing.jsonl` is a machine-readable behavioral regression set. It complements `docs/COMPILER-TESTS.md`; it does not claim to automatically score generated video quality.

Each row contains:
- `input`: user symptom/request;
- `expect`: capabilities/routing behavior that should be represented in planning;
- `avoid`: known failure patterns;
- `mode`: compile or diagnose.

When a real generation experiment changes a canonical behavior rule, update both the owner layer and the relevant eval. Add a new eval only when it protects a reusable behavior, not for every scene reskin.
