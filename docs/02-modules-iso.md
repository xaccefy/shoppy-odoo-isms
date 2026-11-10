# 2. Odoo модуль сонголт ба ISO холбоос (Даалгавар 2)

ISO/IEC 27001:2022 хэрэгжүүлэхэд ашиглах Odoo Community Edition-ийн модулиуд:

| Odoo Module | Харгалзах ISO Control | Яагаад сонгосон бэ? |
|---|---|---|
| Website + eCommerce | A.8.26 Application security, A.8.24 Cryptography (TLS) | shoppy.mn-ийн гол халдлагын гадаргуу — худалдааны вэб; оролт шалгалт, TLS-г энд харуулна |
| Sales | A.8.3 Information access restriction, A.5.19 Supplier relationships | Захиалгын урсгал — борлуулагч зөвхөн өөрийн захиалгыг харах record rule-ийн суурь |
| Contacts | A.5.9 Inventory of information assets, A.5.34 Privacy/PII | Харилцагчийн PII-ийн master data; хандах эрхийн жишээ объект |
| CRM | A.5.34 Privacy, A.8.3 | Харилцагчтай харилцах процесс — хэн юу харж болохыг хязгаарлах |
| Inventory | A.5.9 Inventory of assets | Бараа материалын бүртгэл; мөн ISMS хөрөнгийн бүртгэлийн нэг талбар |
| Invoicing/Accounting | A.8.3, A.5.33 Records protection | Санхүүгийн бичилтийн бүрэн бүтэн байдал — төлбөрийн бичилт өөрчлөгдөхгүй байх |
| Employees (HR) | A.6.1 Screening, A.6.3 Awareness/training, A.6.5 Post-employment | Ажилтны бүртгэл, үүрэг — хүний хяналтуудын суурь |
| Project | A.5.24–A.5.28 Incident management | Helpdesk-ийн оронд: ослын урсгалын 5 үе шаттай kanban самбар + эрсдэлийн бүртгэл |
| Maintenance | A.5.9 Asset inventory, A.7.13 Equipment maintenance | IT тоног төхөөрөмж/системийн хөрөнгийн бүртгэл (Documents Enterprise байхгүй тул) |
| Discuss + Activities | A.6.8 Information security event reporting | Дотоод мэдэгдэл, даалгавар, ослын тайлан өгөх суваг |
| Users & Companies (Settings) | A.5.15–A.5.18, A.8.2, A.8.3, A.8.5 | RBAC-ийн зүрх: бүлэг, record rule, нууц үг, хэрэглэгч |
| Audit Log (OCA) | A.8.15 Logging, A.8.16 Monitoring activities | Community-д audit модуль байхгүй тул OCA `auditlog`-оор бодит log хэрэгжүүлнэ |

## Тайлбар — яагаад эдгээрийг сонгов

1. **Борлуулалтын гол урсгал (Website→Sales→Invoicing→Inventory)** — shoppy.mn-ийн бизнес процессийг бодит ERP болгож, "захиалга→төлбөр→хүргэлт" гинжин дээрх мэдээлэл хаана үүсэж, хэн хүрдэгийг харуулна. Энэ нь asset register-ийн объект юм.

2. **Хяналтын гол суурь (Users & Companies + Audit Log)** — Annex A-ын хамгийн их тохирох хяналт энд байна: хандах эрх (5.15–5.18), privileged access (8.2), logging (8.15). RBAC + audit log нь төслийн заавал хэрэгжүүлэх 2 тохиргоо ч юм.

3. **Хүн ба процесс (Employees, Project, Discuss)** — ISO 27001-ийн хяналтын ~2/3 нь технологи биш удирдлага: ослын урсгал (5.24–5.28) Project-ын stage-ээр, мэдээлэх суваг Discuss-аар, сургалтын бүртгэл HR-аар.

4. **Enterprise орлох шийдлүүд** — Community Edition-д Documents, Helpdesk, Studio байхгүй. Тиймээс:
   - Asset register → **Maintenance** (equipment) + **Inventory** (бараа) + Excel хүснэгт
   - Helpdesk → **Project** app, stage = Incident→Report→Investigate→Resolve→Close
   - Audit trail → **OCA auditlog** (нээлттэй эх) + field tracking (chatter) + `ir.model.metadata`
