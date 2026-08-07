# Real Estate ERP — Odoo 18 Community Addons

**Path:** `/home/abdullah/odoo17-dev/addons/real_estate_erp`  
**Edition:** Odoo 18 Community  
**Local runner:** `./odoo-dev` from `/home/abdullah/odoo17-dev`

## Modules

| Module | Purpose |
|---|---|
| `real_estate` | Meta: install all |
| `real_estate_project` | Projects & flats |
| `real_estate_partner` | Client/dealer fields |
| `real_estate_allotment` | Allot flat to client |
| `real_estate_installment` | Payment targets |
| `real_estate_collection` | Payment submission + approval |
| `real_estate_portal` | Client portal pages |
| `real_estate_dashboard` | Dashboards (later) |
| `real_estate_reports` | Reports (later) |

## Setup Odoo 18 (once)

```bash
cd /home/abdullah/odoo17-dev
docker compose up -d db
./odoo-dev install 18.0
./odoo-dev config 18.0 --write
```

## Create DB & install modules

```bash
cd /home/abdullah/odoo17-dev
./odoo-dev run 18.0 -d re_erp_18 -i real_estate --stop-after-init
./odoo-dev run 18.0 -d re_erp_18
```

Open: **http://localhost:8018**

## Upgrade after code changes

```bash
./odoo-dev run 18.0 -d re_erp_18 -u real_estate_project --stop-after-init
```
