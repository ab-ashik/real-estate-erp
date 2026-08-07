# Local setup notes (Odoo 18 Community)

## Location

- Addons: `/home/abdullah/odoo17-dev/addons/real_estate_erp`
- Runner: `/home/abdullah/odoo17-dev/odoo-dev` (`./odoo-dev`)
- Edition: **Community 18.0**
- DB: `re_erp_18`
- URL: **http://localhost:8018**
- Master password (odoo-dev conf): see `dev/conf/odoo-18-0.conf` (`admin_passwd`)

## Commands

```bash
cd /home/abdullah/odoo17-dev

# Postgres (if down)
docker compose up -d db

# Install Odoo 18 once (already done)
./odoo-dev install 18.0

# Refresh config (addons path includes real_estate_erp only for 18.0)
./odoo-dev config 18.0 --write

# Run
./odoo-dev run 18.0 -d re_erp_18

# Upgrade one module after code changes
./odoo-dev run 18.0 -d re_erp_18 -u real_estate_project --stop-after-init
```

## Modules installed

`real_estate` meta + project, partner, allotment, installment, collection, portal, dashboard, reports.

Scaffold only — business workflows continue in sprints (see proposal `DEVELOPMENT-PLAN.md`).
