# Knowledge Maintenance Protocol

The repository separates **canonical knowledge**, **derived retrieval data**, and **source evidence**.

## Change the owner, not every copy

| Change | Update |
|---|---|
| reusable prompt skeleton | TEMPLATES.md |
| capability/routing concept | CAPABILITIES.md |
| compilation behavior | COMPILER.md |
| general quality rule | PLAYBOOK.md |
| model-specific ruling | docs/最佳实践.md |
| representative example routing | CORE-PICKS.md |
| agent behavior/retrieval | AGENTS.md |
| original/source material | prompts/ or cases/ + source metadata |
| skill trigger/scope | matching skills/*/SKILL.md |

Do not duplicate the same rule into multiple skills.

## Required checks

For source/index changes:

```bash
python3 scripts/build_index.py
python3 scripts/build_index.py --check
python3 scripts/build_agent_index.py
python3 scripts/validate_agent_architecture.py
```

For canonical-rule changes, also update a relevant regression case in `docs/COMPILER-TESTS.md` when behavior changes.

## Agent index

`agent-index.jsonl` is derived from `index.jsonl`. It adds normalized task, model, capability, authority, completeness and retrieval-role hints. Never hand-edit it.

The source index remains authoritative for attribution and original metadata. Retrieval hints are routing aids, not claims that override source evidence.

## Versioning

`agent-manifest.json` contains `knowledge_version`.

- Patch: wording, metadata, retrieval-rule fix without architecture change.
- Minor: new capability family, schema field, model adapter, or canonical workflow behavior.
- Major: incompatible retrieval schema or knowledge-layer ownership change.

Update the version only when consumers need to know the contract changed.

## Deprecation

Do not silently delete a canonical concept that agents may depend on. Replace it, document the new owner/rule, update regression coverage, then remove stale copies.

## Definition of done

A knowledge change is done when:
- the owner layer is updated;
- conflicting copies are absent;
- model/source uncertainty is preserved;
- indexes build deterministically;
- architecture validation passes;
- behavior-changing compiler rules have regression coverage.
