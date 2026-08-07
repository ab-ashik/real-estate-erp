# Branching (simple production style — solo friendly)

Keep it light. You are the only developer; do not over-manage branches.

## Branches we use

| Branch | Purpose |
|---|---|
| `main` | Stable / client-demo ready only |
| `develop` | **Daily work** (default branch) |
| `feature/<name>` | Optional — only for a bigger sprint chunk |

That is enough. No required `release/*` or `hotfix/*` unless you really need them later.

## Day-to-day (solo)

```bash
git checkout develop
git pull

# small work → commit on develop
git add -A
git commit -m "feat: short clear message"
git push origin develop
```

## Bigger sprint (optional feature branch)

```bash
git checkout develop
git pull
git checkout -b feature/sprint-1-security-roles

# ... work, commit ...
git push -u origin feature/sprint-1-security-roles

# when done, merge into develop
git checkout develop
git merge feature/sprint-1-security-roles
git push origin develop
```

## When to update `main`

Only when a milestone is stable (e.g. Sprint 0 done, C1 demo ready):

```bash
git checkout main
git pull
git merge develop
git push origin main
```

Optional tag: `git tag v0.1.0 && git push origin v0.1.0`

## Naming (keep short)

```text
feature/sprint-1-security
feature/allotment-confirm
```

## Rules (simple)

1. Do normal work on **`develop`**
2. Use **`feature/*`** only if the change is large or risky
3. Update **`main`** only for stable milestones
4. Do not force-push `main` or `develop`

## Current

- Repo: `https://github.com/ab-ashik/real-estate-erp.git`
- Sprint 0 scaffold is on `develop` (and feature branch history)
- Default working branch: **`develop`**
