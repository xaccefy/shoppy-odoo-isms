---
marp: true
theme: default
paginate: true
title: ISMS on Odoo ERP — shoppy.mn
---

# Мэдээллийн аюулгүй байдлын удирдлагын систем Odoo ERP дээр

## shoppy.mn — ISO/IEC 27001:2022 хэрэгжүүлэлт

**Баг:** Prost · **Хичээл:** F.NSA338 IS Governance
**Орчин:** Odoo 18 Community + PostgreSQL 16 (Docker)

---

# 1. Байгууллага ба нөхцөл байдал (Clause 4)

- **shoppy.mn** — Монголын хамгийн том B2C цахим худалдааны платформ (хийсвэр кейс)
- Мэдрэмтгий өгөгдөл: харилцагчийн PII, хүргэлтийн хаяг, захиалга, төлбөрийн бичилт
- Гол эрсдэлийн орон: вэб/API, төлбөрийн гарц, хүргэлтийн түншүүд, ажилтнууд
- PESTLE + SWOT-аас гарсан IS зорилтууд:
  - **MFA 100%** — 30 хоногт
  - **RTO ≤ 4 цаг, RPO ≤ 1 цаг**
  - Нийлүүлэгчээс гарах (exit) төлөвлөгөө

---

# 2. Odoo орчин ба Community орлуулга

- **Deployment:** `odoo:18` + `postgres:16` Docker Compose, DB `shoppy`
- Суулгасан: Website/eCommerce, Sales, CRM, Contacts, Inventory, Invoicing,
  HR, Project, Maintenance + OCA **auditlog**, **auth_totp**
- Enterprise → Community орлуулга:
  - Helpdesk → **Project** kanban (5 үе шат)
  - Documents → **Maintenance/Inventory** (asset register)
  - Аудит лог → OCA **auditlog** + Odoo chatter/tracking

---

# 3. Odoo модуль ↔ ISO хяналтын зураглал

| Odoo | ISO/IEC 27001:2022 |
|---|---|
| Website+eCommerce | A.8.26 App security, A.8.24 Crypto |
| Sales/CRM/Contacts | A.8.3 Access restriction, A.5.34 Privacy/PII |
| Inventory + Maintenance | **A.5.9 Asset inventory** |
| Project | **A.5.24–28 Incident management** |
| Employees (HR) | A.6.1–6.8 Хүний хяналт |
| auditlog + chatter | **A.8.15 Logging**, A.8.16 Monitoring |
| auth_totp | **A.8.5 Secure authentication** |

---

# 4. Asset Register (A.5.9) — 14 хөрөнгө

- Бүртгэл Odoo **Maintenance → Equipment** дээр (ASSET-01…14)
- C/I/A тус бүр 1–3, үнэ = max(C,I,A)
- Топ хөрөнгө: харилцагчийн мастер өгөгдөл, захиалга/төлбөр, PostgreSQL,
  админ нэвтрэх мэдээлэл, API түлхүүр, backup багц
- **Нотолгоо:** S04 жагсаалт, S05 ASSET-01 дэлгэрэнгүй

---

# 5. Risk Register + Treatment (Clause 6.1.2–6.1.3)

- Арга: **оноо = нөлөө × магадлал**; 1–6 Бага / 7–12 Дунд / 13–25 Өндөр
- Мөр бүр: аюул занал ≠ эмзэг байдал ≠ **нотолгодсон сул тал**
- Үр дүн: **2 Өндөр** (SQLi R1, backup R3) · 9 Дунд · 1 Бага
- Odoo **Project → "Risk Register"** kanban: Identified→Analysed→Treated→Accepted
- 12/12: treatment + Annex A хяналт + эзэмшигч + residual оноо
- R10 (Бага) — **Accept**: эзэмшигчийн баталгаатай
- **Нотолгоо:** S07 самбар, S08 R1 card

---

# 7. Incident workflow (A.5.24–28)

- Odoo **Project → "Incident Response"** — 5 үе шат:
  **Incident → Report → Investigate → Resolve → Close**
- Жишээ осол: *"Phishing test: 2/10 ажилтан холбоос дарсан"* → Investigate
- Severity tag, эзэмшигч, chatter-ийн timeline — бүртгэлийн мөр
- **Нотолгоо:** S10 самбар, S11 card

---

# 8. ISMS бодлогууд (Task 7)

1. **Мэдээллийн аюулгүй байдлын бодлого** — зорилго, хүрээ, хариуцлага
2. **Хандах эрхийн бодлого** — least privilege, need-to-know, MFA
3. **Backup/Restore бодлого** — RPO ≤1цаг, RTO ≤4цаг, улирал бүр restore test
4. **Incident Response бодлого** — 5 үе шат, мэдээлэх дараалал

*(docs/07-isms-policies.md)*

---

# 9. RBAC + Audit trail (Task 8)

- **5+ бүлэг:** Sales Admin / Sales Own-docs / Inventory User / Auditor (read-only) / ISMS Admin + Auditlog Rights
- **6 хэрэглэгч:** salesmgr, sales1, sales2, wh1, auditor1, isms
- **Record rule баталгаа:** sales1 → зөвхөн өөрийн 2 захиалга (S14)
- **auditlog:** 66 бичилт — хэн/хэзээ/аль model/method (S16–17)
- **auth_totp:** Account Security-д 2FA toggle идэвхтэй (S18)

---

# 10. SoA ба дүгнэлт

- **Statement of Applicability:** 31 Annex A хяналт — Тийм / Хэсэгчилсэн төлөвтэй (docs/08)
- Үлдэгдэл эрсдэл: Өндөр 2 → Бага 2 (treatment-ийн дараа, эзэмшигч баталгаатай)
- **Цаашид:** MFA rollout → penetration test → BCP drill → ISO 27001 баталгаажуулалт

---

# 11. Live Demo (10–15 мин)

1. Company → `Shoppy.mn LLC`, Улаанбаатар (S03)
2. Apps → суулгасан модулиуд + Enterprise "Upgrade" нотолгоо (S02)
3. Maintenance → Asset register ASSET-01…14 (S04–05)
4. Project → Risk Register kanban + R1 card (S07–08)
5. Project → Incident board 5 stage + phishing card (S10–11)
6. Settings → Groups/Users + **sales1-ээр нэвтэрч** record rule харуулах (S12–14)
7. Settings → Technical → Audit → Logs (S16)

**Баярлалаа — Асуулт?** Prost · Seminar 6–7 + LAB-10 материал ашигласан
