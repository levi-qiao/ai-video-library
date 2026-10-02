# PROMPT COMPILER

Purpose: turn a short request into an executable AI-video prompt without copying whole examples.

## Pipeline

1. Parse: task, model, duration, aspect ratio, subject anchors, scene, core event, references, preferences, constraints.
2. Route: choose exactly one skeleton from TEMPLATES.md.
3. Select: choose 3-5 capabilities from CAPABILITIES.md.
4. Blueprint: plan each shot as framing | action | result | main camera move | environment response | end state.
5. Materialize: translate capability names into visible actions and camera behavior.
6. Adapt: apply model rules from docs/最佳实践.md.
7. Lint: fix identity, spatial, causal, camera, continuity, syntax, and redundancy problems.
8. Emit: by default return only the copy-ready prompt.

## Parse rules

Ask a question only when the core event cannot be determined. Missing style or aspect ratio normally does not block compilation. Use 2-3 stable subject anchors; use A/B for multiple characters. Treat style words as variables such as material, palette, lighting, and VFX language.

## Selection rules

Use one main structure, one main camera intention, and only the feedback/style capabilities needed for the task. If several camera moves compete in one shot, keep one or split the shot. If a fast sequence requests slow motion everywhere, reserve slow motion for key contacts. If several VFX languages compete, keep one dominant language.

## Blueprint rules

For fights, every important hit follows: force generation -> contact -> reaction -> camera response -> environment response. A generation segment normally contains 1-2 key moves. Overall intensity comes from progression across segments, not from stuffing one segment.

## Materialization examples

- force chain: right foot drives into the ground, hips rotate, shoulder follows, blade rises diagonally.
- contact/reaction: blade spine hits the blocking sword; defender's arms drop and center of gravity shifts backward.
- particle response: water and gravel burst backward along the force direction.
- occlusion reveal: camera begins behind foreground bamboo leaves; the fighter breaks through the gap into view.
- ink VFX: ink dry-brush marks appear only along the real blade path and contact point.

Capability names are planning metadata. Do not dump them verbatim into the final prompt.

## Model adaptation

Follow docs/最佳实践.md as the canonical source. Seedance 2.0 uses shot labels rather than precise timestamp control; Seedance 2.5 may use continuous integer-second ranges; Kling 3.0 uses Shot N (Xs); Runway Gen-4 treats a 5-10s clip as one scene and does not rely on negative phrasing; Veo uses natural-language structure with a separate negative list. For an unknown model, use natural language plus shot labels and do not invent model features.

## Lint

Errors to fix before output: identity conflict, contradictory spatial relation, competing main camera moves, strong reaction without readable contact, destroyed environment resetting, incompatible model syntax.

Warnings to compress: repeated quality slogans, emotion adjectives without visible behavior, global rules repeated in every shot, untriggered VFX, too many key actions in one segment, more than five capabilities without a clear reason.

## Output contract

Default output: one copy-ready final prompt. If explanation is requested, add only the selected capabilities, one primary template/example reference (optionally one secondary), model-specific adaptation that changed the wording, and unresolved uncertainty.

## Routing examples

"Fight feels weak" -> force chain + contact/reaction + contact-point priority.
"They stand still" -> continuous pursuit + terrain route + terrain-assisted repositioning.
"Ink looks pasted on" -> trajectory anchoring + 2D-in-3D + particle response.
"Vlog looks like an ad" -> event priority + handheld imperfection.
"Make the climax stronger" -> light/heavy/finisher hierarchy + brief contact hold + post-burst slowdown.

## Minimal instruction

Parse the request; choose one TEMPLATES skeleton; choose 3-5 CAPABILITIES; use at most one primary and one secondary CORE-PICKS example; blueprint before prose; materialize every capability into visible action; apply PLAYBOOK and model rules; lint continuity and redundancy; emit the usable prompt first.
