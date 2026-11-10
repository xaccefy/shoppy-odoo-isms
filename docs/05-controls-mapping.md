# 5. ISO/IEC 27001:2022 Annex A → Odoo Controls Mapping (Даалгавар 5)

Annex A-аас сонгосон 30 хяналт бүрийг Odoo дээр хэрхэн хэрэгжүүлснийг харуулна. "Odoo Implementation" багана = бодит тохиргоо/механизм; нотолгооны скриншотын дугаарыг тайлангийн хавсралтад заав.

## A.5 — Удирдлагын хяналтууд (Organizational)

| Control | Тодорхойлолт | Odoo Implementation |
|---|---|---|
| A.5.1 | Мэдээллийн аюулгүй байдлын бодлогууд | ISMS бодлогын баримт бичигүүд (Task 7) — Odoo-ын Discuss/notes-д нийтэлж, харилцах бүлэгт хүргэв |
| A.5.3 | Үүргийн тусгаарлалт (Segregation of duties) | Sale confirm ≠ delivery validate ≠ invoice: тусдаг бүлгийн эрхээр (Sales Manager vs Staff vs Warehouse) |
| A.5.9 | Хөрөнгийн бүртгэл | Maintenance equipment + Inventory бүртгэл; asset register 14 мөр (Task 3) |
| A.5.15 | Хандах эрхийн удирдлага (Access control) | Settings→Users & Companies→Groups: 5 бүлэг, menu/model access, record rules |
| A.5.16 | Таних системийн удирдлага (Identity mgmt) | Хэрэглэгч бүр тусдаг account; деактив хийх механизм; "Manage Access Rights" дэлгэц |
| A.5.17 | Нэвтрэх мэдээлэл (Authentication info) | Нууц үгийн policy, password reset урсгал, session timeout |
| A.5.18 | Хандах эрхийн олголт/хураалт | Бүлэгт оруулах/гарах → эрх шууд өөрчлөгдөнө; audit demo: бүлэг солиход харагдах өгөгдөл өөрчлөгдөнө |
| A.5.19 | Түншүүдийн харилцааны АБ | Purchase/Contacts-д төлбөрийн гарц, cloud, хүргэлтийн түншийг vendor бүртгэл болгож, гэрээ/SLA хавсаргана |
| A.5.20 | Түншийн гэрээний АБ нөхцөл | Vendor record дээр АБ заалт + хавсралт баримт (SLA, data-sharing) |
| A.5.23 | Cloud үйлчилгээний АБ | Deployment бодлого: Docker-орсон үйлчилгээ, backup-offsite, exit plan (PESTLE-P) |
| A.5.24 | Инцидент менежментийн төлөвлөгөө | Project "Incident Response" самбар, 5 stage урсгал (Task 6) |
| A.5.25 | Инцидентыг үнэлэх, шийдвэрлэх | Stage "Investigate"+severity tag; даалгаврын дотор үнэлгээний бичилт |
| A.5.26 | Инцидентэд хариу өгөх | Stage "Resolve": эзэмшигч, хугацаа, сэргээсэн үйлдэл |
| A.5.27 | Инцидентээс суралцах | Stage "Close": postmortem тэмдэглэл, давтагдсан шинжээр tag → risk register рүү буцах |
| A.5.28 | Нотолгоо цуглуулах | Инцидент карт дээрх chatter + хавсралт + auditlog бичилт хавсаргана |
| A.5.29 | Тасралтгүй байдлын төлөвлөгөө | Backup журам + restore test-ийн баримт (RPO ≤1ц/RTO ≤4ц бодлогоос) |
| A.5.34 | Хувийн мэдээлэл/PII хамгаалал | res.partner дээр record rule; хүргэлтийн export-аас PII талбар хасах (R5); зөвшөөрлийн талбар |

## A.6 — Хүний хяналтууд (People)

| Control | Тодорхойлолт | Odoo Implementation |
|---|---|---|
| A.6.3 | АБ мэдлэг, сургалт | Employees bүртгэл + Discuss-ын сургалтын сувag; phishing тестийн үр дүн харилцах |
| A.6.8 | АБ үйл явдлыг мэдээлэх суваг | Project самбарын "Incident" stage-д ажилтан бүр карт үүсгэж мэдээлнэ (Report channel) |

## A.8 — Технологийн хяналтууд (Technological)

| Control | Тодорхойлолт | Odoo Implementation |
|---|---|---|
| A.8.2 | Privileged access | Administration/Settings бүлэг зөвхөн ISMS admin; бусдад "no admin" — superuser-гүй бодит бүлэг |
| A.8.3 | Мэдээлэлд хандах хязгаар | Record rule: sales staff зөвхөн өөрийн захиалга; auditor бүлэг read-only |
| A.8.5 | Аюулгүй нэвтрэлт | Нууц үг + MFA (TOTP — Users→Preferences→Two-factor); session хугацаа |
| A.8.8 | Техникийн эмзэг байдлын удирдлага | Odoo/OCA модулиудын хувилбар хяналт (git), image pin (odoo:18 tag), patch журам |
| A.8.9 | Тохиргооны удирдлага | `odoo.conf` git-д; admin_passwd env; `list_db=False`, `proxy_mode=True` baseline |
| A.8.13 | Өгөгдлийн backup | Postgres dump + filestore volume snapshot-ийн журам; restore test-ийн бичилт |
| A.8.15 | Logging | OCA `auditlog` (res.partner, sale.order дээр create/write/delete log) + odoo.log + chatter tracking |
| A.8.16 | Хяналт-шинжилгээний үйл ажиллагаа | auditlog дээр хайлт/шүүлт; хэнд хэзээ өөрчлөлт хийснийг гаргаж үзэх demo |
| A.8.24 | Криптограф | TLS proxy_mode; нууц үг PBKDF2 hash (Odoo стандарт); API түлхүүр env-ээр, config-д биш |
| A.8.26 | Application security | ORM parameterized query (SQLi хамгаалалт); CSRF token; ORM input validation |
| A.8.28 | Secure coding | OCA/өөрийн кодод ORM-д хатуу хэлбэр; `requests`/`env` secrets-кодонд биш |

*(30 хяналт — даалгаврын 20–25 шаардлагаас давуулсан; тайланд тус бүрт дэлгэцийн зургийн дугаар холбоно.)*

## SoA-гийн суурь

Дээрх хяналт бүр SoA хүснэгтийн мөр болно: **Тийм** (хэрэгжсэн, нотолгоотой) / **Үгүй** (Community хязгаарлалт — жиш нь A.8.6 capacity) / **Хэсэгчилсэн** (A.8.21 network segregation — Docker bridge-ээр хязгаарлагдсан ч бүрэн сегмент биш).
