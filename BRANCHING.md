# Branching model (production-house style)

Even with a single developer, we keep clear branches so releases stay safe.

## Branches

| Branch | Purpose | Who merges |
|---|---|---|
| `main` | Production-ready only (tagged releases) | Via PR from `release/*` or `hotfix/*` |
| `develop` | Integration branch — accepted work ready for next release | Via PR from `feature/*` |
| `feature/*` | Active development | Developer |
| `release/*` | Release prep / freeze (optional) | From `develop` → then to `main` |
| `hotfix/*` | Urgent production fixes | Into `main` and back to `develop` |

## Naming

```text
feature/sprint-0-odoo18-scaffold
feature/sprint-1-security-roles
feature/allotment-confirm-lock-flat
hotfix/fix-allottee-status-label
release/1.0.0
```

## Solo workflow (still production style)

1. Start from latest `develop`:
   ```bash
   git checkout develop
   git pull
   git checkout -b feature/<short-name>
   ```
2. Commit on the feature branch (small, clear commits).
3. Push feature branch and open PR → `develop`.
4. When a release is ready: PR `develop` → `main` (or `release/x.y.z` → `main`).
5. Tag on `main`: `v1.0.0`.

## Never

- Commit directly to `main` for normal work  
- Force-push `main` / `develop`  
- Mix unrelated features on one long-lived feature branch  

## Current state

- Sprint 0 scaffold landed on `feature/sprint-0-odoo18-scaffold` and merged to `develop`.
