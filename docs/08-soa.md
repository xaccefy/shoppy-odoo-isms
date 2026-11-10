# 8. Statement of Applicability (SoA) — shoppy.mn

Annex A хяналт бүрийг хэрэгжсэн эсэх, шалтгаан/үндэслэлээр. (Тайлангийн хүснэгт — Task 5-ын 30 хяналтаас өргөтгөж нийт 31 мөр.)

| Annex A Control | Хэрэгжсэн үү? | Тайлбар / Шалтгаан, үндэслэл |
|---|---|---|
| A.5.1 IS policies | Тийм | ISMS-POL-01 батлагдсан (Task 7) |
| A.5.3 Segregation of duties | Тийм | Sales Manager / Staff / Warehouse бүлгүүдээр confirm≠deliver≠invoice |
| A.5.9 Asset inventory | Тийм | Maintenance + Inventory-р 14 хөрөнгө бүртгэсэн (Task 3) |
| A.5.15 Access control | Тийм | 5 RBAC бүлэг + record rules (Task 8) |
| A.5.16 Identity mgmt | Тийм | Хэрэглэгч бүр тусдаг, деактив механизмтай |
| A.5.17 Authentication info | Тийм | Нууц үг hash; MFA policy бодлогоор заасан |
| A.5.18 Access rights provision | Тийм | Бүлэг солих → эрх шууд өөрчлөгдөх demo |
| A.5.19 Supplier relationships | Хэсэгчилсэн | Vendor бүртгэлд АБ заалт; гэрээний SLA текст хязгаарлагдмал |
| A.5.20 Supplier agreements | Хэсэгчилсэн | Адилхан — vendor record + хавсралт |
| A.5.23 Cloud services | Хэсэгчилсэн | Бодлого + exit plan байна; бодит multi-cloud failover байхгүй |
| A.5.24 Incident planning | Тийм | Project самбар, 5 stage (Task 6) |
| A.5.25 Incident assessment | Тийм | Investigate stage + severity tag |
| A.5.26 Incident response | Тийм | Resolve stage, эзэмшигчтэй |
| A.5.27 Learning from incidents | Тийм | Close stage postmortem → risk register рүү буцах |
| A.5.28 Evidence collection | Хэсэгчилсэн | Chatter + auditlog хавсралт; албан forensic процесс байхгүй |
| A.5.29 Continuity | Хэсэгчилсэн | Backup журам + restore test төлөвлөгөө; failover байхгүй |
| A.5.34 PII protection | Хэсэгчилсэн | Record rule + export хязгаарлалт; бүрэн DPO процесс байхгүй |
| A.6.3 Awareness/training | Хэсэгчилсэн | Phishing тестийн үр дүн бүртгэсэн; тогтмол хөтөлбөр төлөвлөгдсөн |
| A.6.8 Event reporting channel | Тийм | Аливаа ажилтан Incident stage-д карт үүсгэж чадна |
| A.8.2 Privileged access | Тийм | Admin эрх зөвхөн ISMS Admin бүлэгт |
| A.8.3 Access restriction | Тийм | Record rule demo: sales staff зөвхөн өөрийн захиалга |
| A.8.5 Secure authentication | Тийм | Нууц үг + MFA (TOTP) Users→Preferences |
| A.8.8 Vulnerability mgmt | Хэсэгчилсэн | Хувилбар pin (odoo:18), patch журам; скан хөтөлбөр байхгүй |
| A.8.9 Configuration mgmt | Тийм | odoo.conf git-д baseline; list_db=False, proxy_mode |
| A.8.13 Backup | Тийм | pg_dump + volume snapshot журам, restore test бичилттэй |
| A.8.15 Logging | Тийм | OCA auditlog + odoo.log + chatter |
| A.8.16 Monitoring | Хэсэгчилсэн | auditlog хайлт гар аргаар; SIEM/alert байхгүй |
| A.8.21 Network services | Хэсэгчилсэн | Docker bridge isolation; WAF/rate-limit төлөвлөгдсөн (R6) |
| A.8.24 Cryptography | Тийм | TLS proxy, PBKDF2 password hash |
| A.8.26 Application security | Тийм | ORM parameterized queries, CSRF |
| A.8.28 Secure coding | Хэсэгчилсэн | ORM convention; кодын review процесс төлөвлөгдсөн |

**SoA-ын дүгнэлт:** 30 хяналтаас Тийм=19, Хэсэгчилсэн=11, Үгүй=0. "Хэсэгчилсэн" бүхэд тайлангийн 10-р хэсэгт сайжруулах санал болгож бичнэ.
