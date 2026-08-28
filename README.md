# orchestrating-econometric-research

A reusable Codex/Agent Skill for persistent, auditable empirical econometric research.

## Install

Copy this directory to the cross-runtime skills location:

```text
~/.agents/skills/orchestrating-econometric-research/
```

On Windows, `~` refers to your user home. For example, the directory is typically under your user profile's `.agents/skills/` folder.

## Use

In Codex, ask for the skill explicitly or give a task that matches its trigger, for example:

```text
Use the orchestrating-econometric-research skill to audit and initialize this empirical project.
```

or:

```text
Use the econometric research workflow to continue from PROJECT_STATE.yaml.
```

## Non-destructive project initialization

```bash
python ~/.agents/skills/orchestrating-econometric-research/scripts/init_project.py .
python ~/.agents/skills/orchestrating-econometric-research/scripts/validate_project.py .
```

The initializer creates only missing contract files/directories. It does not overwrite existing project files.

## Contents

- `SKILL.md` — triggering and orchestration rules.
- `references/` — detailed econometric/data/IV/search protocols.
- `templates/` — reusable project contracts and review records.
- `scripts/` — non-destructive initialization and validation tools.
- `tests/` — structural tests and pressure scenarios for future behavior validation.
