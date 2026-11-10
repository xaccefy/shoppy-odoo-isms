# Odoo ERP + ISO/IEC 27001:2022 — Project Plan (team Prost)

**Case:** shoppy.mn — "Mongolia's largest e-commerce platform" (fictional; already used in Seminars 1, 2, 6–7)
**System:** Odoo 18 Community Edition, Docker Compose (Brief Option A)
**Due:** report + screenshots + slides → end of week 12; defense + live demo 10–15 min → week 13
**Grading /10:** practical implementation 3.0 · ISO mapping 2.0 · completeness 2.0 · understanding 1.5 · documentation 1.5

## Sources already on disk (reuse, don't redo)

| Source | Feeds |
|---|---|
| `sem10/Seminar10_Prost.xlsx` (LAB-10 workbook) | register format, scoring scheme, thresholds, 4 treatment variants |
| vault `Seminar 6 7-ISO27001-Context-Policy.md` | Task 1 (Clause 4: PESTLE, SWOT, 7 interested parties) + Task 7 (IS policy w/ MFA 100%/30d, RTO ≤4h, RPO ≤1h) |
| vault `Seminar 1 CIA-AAA.md` | CIA classification vocabulary for asset register |
| vault `Seminar 2 Ethics-Law-Standards.md` | e-commerce risks: data leakage, payment fraud, trust loss, legal liability |
| vault `Lectures/Risk Management.md` | 5-step cycle, impact×likelihood, SoA justification rule |

**Known shoppy.mn facts to keep consistent:** centralised order system; card data NOT stored (payment gateway); MFA partly deployed; restore testing erratic; foreign cloud, payment gateway and delivery partners; data = customer personal data, delivery addresses, orders, payment records.

## Community Edition substitutions (flag in report — shows understanding)

| Brief assumes | Community reality | We use instead |
|---|---|---|
| Documents module | Enterprise only | Maintenance (equipment register) + Inventory (products) |
| Helpdesk module | Enterprise only | Project app, kanban stages = Incident→Report→Investigate→Resolve→Close |
| Audit log | No built-in module | OCA `auditlog` (free, server-tools) + field tracking/chatter + metadata |
| Risk module | none | Project app "Risk Register" project + Excel register |

## Execution order

### Phase 0 — Environment (Day 1)
- [ ] `docker-compose.yml`: odoo:18 + postgres:16, named volumes, port 8069
- [ ] `odoo.conf`: admin passwd, addons path incl. `./addons` for OCA
- [ ] Up, create DB `shoppy`, login → **screenshot S00** (Week-1 checkpoint: Odoo-д нэвтэрсэн дэлгэц)

### Phase 1 — Tasks 1–2: Context & module selection (Day 1–2)
- [ ] Task 1 doc (`docs/01-context.md`): Clause 4 analysis for shoppy.mn — reuse Sem6-7 PESTLE/SWOT/interested parties verbatim-quality, add ISMS scope statement + ½-page org intro (Week-1 checkpoint)
- [ ] Install apps: eCommerce(website_sale), Sales, CRM, Inventory, Invoicing, Contacts, Employees, Project, Maintenance, Discuss, Settings
- [ ] Task 2 table (`docs/02-modules-iso.md`): each module ↔ Annex A control(s) ↔ why chosen. e.g. Sales→A.5.19/A.8.9? Draft below.
- [ ] Create company "Shoppy.mn LLC", admin user → **screenshots S01–S03** (apps list, company settings)

### Phase 2 — Task 3: Asset Register (Day 2–3)
- [ ] ≥12 assets (buffer over the required 10), each: name, owner, classification (Confidential/Internal/Public), location, C/I/A 1–3, value=max, risk L/M/H
- [ ] Enter in Odoo: data assets → Maintenance equipment or Inventory items; write Excel register sheet too (workbook format, 27 cols)
- [ ] Candidate assets: customer DB, order/payment records, web storefront (website_sale), PostgreSQL server, admin accounts/credentials, Odoo configs, backup sets, API keys (payment gateway), delivery-partner data feed, staff laptops, session/log data, product catalogue
- [ ] **Screenshots S04–S06** (asset list in Odoo, one asset detail, classification)

### Phase 3 — Task 4: Risk Assessment (Day 3–4)
- [ ] ≥12 risks; each: threat, vulnerability, **weakness found by assessment** (evidence sentence — the workbook discipline), impact 1–5, likelihood 1–5, score, level, decision, owner, treatment, Annex A controls, residual + approval date
- [ ] Seed candidates from vault: SQLi on shop search, no MFA on all staff, backups untested, payment-gateway API key exposure, delivery API over-shared PII, DDoS on promo days, phishing staff, misconfigured cloud bucket, insider order tampering, unpatched Odoo, lost laptop w/ saved session, log retention gap
- [ ] Odoo Project "Risk Register": stages = identified/analysed/treated/accepted; one task per risk w/ score in description → **screenshots S07–S09**

### Phase 4 — Task 5: Controls Mapping (Day 4–5)
- [ ] 22–25 Annex A controls, table: control → description → Odoo implementation → evidence (screenshot ref)
- [ ] Draft set: A.5.1, A.5.9, A.5.15, A.5.16, A.5.17, A.5.18, A.5.19, A.5.20, A.5.23, A.6.3, A.7.10, A.8.2, A.8.3, A.8.5, A.8.7, A.8.8, A.8.9, A.8.13, A.8.15, A.8.16, A.8.20, A.8.22, A.8.24, A.8.28

### Phase 5 — Task 6: Incident Management (Day 5)
- [ ] Project "Incident Response" board: 5 stages Incident→Report→Investigate→Resolve→Close + tags (severity), auto-assign, activities
- [ ] Workflow diagram (mermaid + PNG for report) → **screenshots S10–S11**

### Phase 6 — Task 7: ISMS Documents (Day 5–6)
- [ ] Pick 3: (a) Information Security Policy — adapt Sem6-7 version w/ 3 measurable objectives; (b) Access Control Policy — matches our RBAC groups; (c) Risk Treatment Plan — from Task 4 register. Each 1–2 pp, Mongolian.

### Phase 7 — Task 8: Implementation + SoA (Day 6–7)
- [ ] RBAC: 5 groups — e.g. `ISMS Admin`, `Sales Manager`, `Sales Staff`, `Warehouse`, `Auditor (read-only)`; record rules so sales staff see own orders only → **S12–S14**
- [ ] ≥5 users (one per role) + login/activity demo → **S15**
- [ ] Audit log: OCA auditlog on res.partner + sale.order; fallback = field tracking + chatter → **S16–S17**
- [ ] SoA table: every selected Annex A control → Тийм/Үгүй/Хэсэгчилсэн + justification → `docs/08-soa.md`

### Phase 8 — Assemble & defend (Day 8–10)
- [ ] `report/`: final report (11 sections per brief §6, 20–30 pp) — write in Mongolian, export DOCX/PDF (pandoc)
- [ ] Slides 8–12 (marp or pptxgenjs): case→modules→assets→risks→mapping→incident→RBAC/SoA→demo→lessons
- [ ] `docs/ai-disclosure.md` → disclosure paragraph at end of report (ethics §9)
- [ ] `docs/demo-script.md`: 10–15 min live path through Odoo
- [ ] Screenshot index `screenshots/INDEX.md` — every shot numbered, captioned, referenced in report

## Report skeleton (brief §6, 11 sections)
1. Cover — shoppy.mn, team members, date
2. Intro + org presentation
3. Module selection + ISO link
4. Asset Register
5. Risk Assessment
6. ISO Controls Mapping
7. Incident Management flow
8. ISMS policy docs
9. Implementation evidence (RBAC, audit log) + SoA
10. Conclusion: challenges, lessons, improvements
11. Appendix: screenshots, sources, **AI-use disclosure**

## Principles
- Every screenshot = real Odoo state on this machine; nothing mocked (ethics §9).
- Register discipline: threat ≠ vulnerability ≠ weakness-found; formulas compute scores; owner + date on residual.
- Mongolian for all submitted docs; Odoo/technical terms stay English (brief allows).
- Freeze scoring thresholds (0–6 / 7–12 / 13–25) before scoring — same as workbook.
