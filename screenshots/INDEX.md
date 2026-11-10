# Screenshot index — shoppy.mn Odoo ISMS

Бүх зураг `screenshots/` дотор `S##_description.png` нэртэй. Тайланд дугаараар ишлэнэ.
Огноо: 2026-11-11, Odoo 18 Community, DB `shoppy`, http://localhost:8069

| № | Файл | Агуулга | Task / Checkpoint |
|---|---|---|---|
| S00 | S00_login.png | Odoo login дэлгэц (database `shoppy`) | Week-1 checkpoint |
| S01 | S01_backend_home.png | Backend home — бүх app-ууд (Shoppy.mn LLC) | Task 2 |
| S02 | S02_apps.png | Суулгасан Apps жагсаалт (auditlog, auth_totp оролцуулсан; Enterprise "Upgrade" товчууд харагдана → Community орлуулга нотолгоо) | Task 2 |
| S03 | S03_company_settings.png | General Settings — Company "Shoppy.mn LLC", Peace Avenue 15, Улаанбаатар; 7 хэрэглэгч | Task 1/2 |
| S04 | S04_equipment_list.png | Asset register — Maintenance→Equipment, 14 ISMS asset (ASSET-01…14) | Task 3 |
| S05 | S05_asset_detail.png | ASSET-01 дэлгэрэнгүй — төрөл, эзэмшигч, ISMS classification тэмдэглэл | Task 3 |
| S06 | S06_contacts.png | Contacts — зөвхөн shoppy.mn өгөгдөл (3 харилцагч + 6 ажилтан + компани) | Task 3 / demo data |
| S07a | S07a_projects.png | Projects жагсаалт — `Risk Register`, `Incident Response` | Task 4/6 |
| S07 | S07_risk_register.png | Risk Register kanban — 4 stage, 12 оноосон эрсдэл | Task 4 |
| S08 | S08_risk_card.png | R1 SQL injection card — threat/vulnerability/weakness/treatment/Annex A | Task 4 |
| S10 | S10_incident_board.png | Incident Response kanban — 5 stage (Incident→Report→Investigate→Resolve→Close) | Task 6 |
| S11 | S11_incident_card.png | Phishing-test incident card — severity tag, Investigate stage | Task 6 |
| S12 | S12_groups_list.png | Groups жагсаалт — 83 бүлэг (Auditlog Rights, Admin/Technical багцууд) | Task 8 / A.5.15 |
| S13 | S13_group_sales_owndocs.png | `Sales / User: Own Documents Only` бүлэг — 5 гишүүн, Record Rules tab | Task 8 / A.8.3 |
| S14 | S14_sales1_restricted.png | `sales1` хэрэглэгчээр — зөвхөн өөрийн 2 quotation (record rule ажилласан нотолгоо) | Task 8 / A.8.3 |
| S15 | S15_users_list.png | Users жагсаалт — 6 шинэ хэрэглэгч + admin | Task 8 / A.5.16 |
| S16 | S16_auditlog.png | Audit Logs — 66 бичилт: хэн/хэзээ/аль model/янз method (Sarnai Sales-ийн write оролцуулсан) | Task 8 / A.8.15 |
| S17 | S17_auditlog_rules.png | Audit Rules тохиргоо — Contact, Sales Order log_capture | Task 8 / A.8.15 |
| S18 | S18_user_2fa.png | Account Security tab — Two-Factor Authentication toggle (auth_totp идэвхтэй; 30 хоногт 100% зорилгын суурь) | A.8.5 |

Тэмдэглэл:
- S09 (risk stage-ээр filter) — S07 дээр stage-ийн тоолуур аль хэдийн харагддаг тул тусгаарлаагүй.
- Демо хэрэглэгчийн нууц үг `shoppy123` нь зөвхөн локал хичээлийн орчинд зориулсан; production тохиргоо биш.
