#!/usr/bin/env bash
# Assemble REPORT.md from docs/ + screenshot appendix, then render to .docx
# Usage: bash scripts/build_report.sh
set -e
cd "$(dirname "$0")/.."

OUT=report
mkdir -p "$OUT"

cat > "$OUT/REPORT.md" <<'HEADER'
---
title: "Мэдээллийн аюулгүй байдлын удирдлагын систем (ISMS) — Odoo ERP дээрх хэрэгжүүлэлт"
subtitle: "shoppy.mn — цахим худалдааны платформ | ISO/IEC 27001:2022"
author: "Баг: Prost"
date: "Хичээл: F.NSA338 Information Security Governance | 2026 оны намар"
---

**Даалгаврын товч.** Энэхүү тайланд shoppy.mn (хийсвэр Монгол цахим худалдааны платформ)-ын
ISMS-ийг Odoo 18 Community орчинд бодитоор хэрэгжүүлсэн ажлыг тайлбарлав.
Даалгавар бүр Odoo дахь бодит тохиргоогоор нотлогдоно — дэлгэцийн зургууд
хавсралтад (Бүлэг 11) эмхэтгэв.

**Орчны мэдээлэл:** Odoo 18 Community (Docker image `odoo:18`), PostgreSQL 16 (`postgres:16`),
database `shoppy`, URL http://localhost:8069. Суулгасан нэмэлт: OCA `auditlog` (server-tools 18.0),
`auth_totp`. Community Edition-ийн хязгаарлалт тухайд: Documents ба Helpdesk нь Enterprise-only
тул хөрөнгийн бүртгэлийг Maintenance/Inventory-аар, ослын урсгалыг Project kanban-аар орлуулсан —
өнөөдрийг хүртэл энэ нь курсын дүрэмд нийцнэ.

HEADER

for f in docs/01-context.md docs/02-modules-iso.md docs/03-asset-register.md \
         docs/04-risk-register.md docs/05-controls-mapping.md \
         docs/06-incident-management.md docs/07-isms-policies.md docs/08-soa.md; do
  cat "$f" >> "$OUT/REPORT.md"
  printf '\n\n' >> "$OUT/REPORT.md"
done

cat >> "$OUT/REPORT.md" <<'APX'

# 11. Дэлгэцийн зургийн хавсралт (Odoo Configuration Archive)

Доорх зургууд бүгд ажиллаж буй локал Odoo 18 орчноос авсан бодит зураг.
Дугаарлалт: `screenshots/INDEX.md`-тай ижил.

APX

# Build appendix entries from INDEX.md table rows
python3 - <<'PY'
import re
rows = []
for line in open('screenshots/INDEX.md', encoding='utf-8'):
    m = re.match(r'\| (S\d+a?) \| (\S+\.png) \| (.+?) \|', line)
    if m:
        rows.append(m.groups())
with open('report/REPORT.md', 'a', encoding='utf-8') as f:
    for sid, fn, desc in rows:
        f.write(f'## {sid} — {desc}\n\n')
        f.write(f'![{sid}](screenshots/{fn})\n\n')
PY

cat docs/ai-disclosure.md >> "$OUT/REPORT.md"

pandoc "$OUT/REPORT.md" -o "$OUT/REPORT.docx" \
  --toc --toc-depth=2 \
  --resource-path=. \
  -V geometry:margin=2.5cm \
  --metadata lang=mn

echo "==> $OUT/REPORT.docx built"
ls -la "$OUT/"
