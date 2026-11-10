# shoppy.mn ISMS on Odoo 18 — ISO/IEC 27001 coursework (team Prost)

F.NSA338 Information Security Governance team project: implement an ISMS for the
fictional Mongolian e-commerce platform **shoppy.mn** on a real Odoo 18 Community
deployment, evidenced by screenshots and a live demo.

## Deliverables

| Item | Location |
|---|---|
| Unified report (~40pp + screenshot appendix) | `report/REPORT.docx` / `REPORT.pdf` |
| Presentation (12 slides) | `report/slides.pptx` (+ `slides.md`) |
| Screenshot archive (19 shots, indexed) | `screenshots/` + `INDEX.md` |
| Chapter docs (source of truth) | `docs/01`–`08`, `ai-disclosure`, `demo-script` |

## Reproduce the environment

```bash
docker compose up -d
# init DB `shoppy` with modules (first boot):
docker exec -it shoppy_odoo odoo -d shoppy -i \
  web,base_setup,website,website_sale,sale_management,crm,account,stock,purchase,\
  contacts,hr,project,maintenance,auditlog,auth_totp --stop-after-init --without-demo=all
docker restart shoppy_odoo
python3 scripts/setup_odoo.py   # company, users, groups, projects, assets, risks, audit rules
```

- Odoo: http://localhost:8069 (admin/admin — local demo only)
- OCA `auditlog` (server-tools 18.0) is vendored in `addons/` so the stack works offline.
- Demo user passwords (`shoppy123`) and `admin_passwd` in `config/odoo.conf`
  are **local coursework values, not production secrets**.

## Rebuild the report

```bash
bash scripts/build_report.sh                          # REPORT.md → REPORT.docx
libreoffice --headless --convert-to pdf report/REPORT.docx
pandoc report/slides.md -o report/slides.pptx --slide-level=1
```

## Layout

```
├── docker-compose.yml    # odoo:18 + postgres:16
├── config/odoo.conf      # Odoo server config
├── addons/auditlog/      # OCA audit trail module
├── scripts/              # XML-RPC setup + report builder
├── docs/                 # 8 assignment chapters + SoA + disclosure + demo script
├── screenshots/          # S00–S18 evidence + INDEX.md
├── report/               # assembled report + slides
└── PLAN.md               # project plan
```
