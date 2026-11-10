# 3. Asset Register — shoppy.mn (Даалгавар 3)

ISO/IEC 27001:2022, A.5.9 (Inventory of information and other associated assets)-ын дагуу shoppy.mn-ийн мэдээллийн хөрөнгийн бүртгэл. Үнэлгээ: C/I/A тус бүр 1–3, хөрөнгийн үнэ = max(C,I,A) (3→Өндөр, 2→Дунд, 1→Бага). Бүртгэлийг Odoo-д (Maintenance/Inventory модуляар) орсон бөгөөд дэлгэцийн зураг тайланд хавсаргав.

| № | Хөрөнгө (Asset) | Төрөл | Owner | Classification | Location | C | I | A | Үнэ | Risk |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Харилцагчийн мастер өгөгдөл (нэр, утас, имэйл, хүргэлтийн хаяг) | Өгөгдөл | Үйл ажиллагааны захирал | Confidential | Odoo Contacts / PostgreSQL | 3 | 3 | 2 | Өндөр | Өндөр |
| 2 | Захиалга ба төлбөрийн бичилт (захиалгын түүх, гүйлгээний статус) | Өгөгдөл | Борлуулалтын захирал | Confidential | Odoo Sales / Invoicing | 3 | 3 | 3 | Өндөр | Өндөр |
| 3 | Вэб дэлгүүр (storefront, website_sale) | Програм | CTO | Internal | Docker host :8069 | 2 | 3 | 3 | Өндөр | Өндөр |
| 4 | Odoo ERP систем (backend, бизнес логик) | Систем | CTO | Internal | odoo container | 3 | 3 | 3 | Өндөр | Өндөр |
| 5 | PostgreSQL өгөгдлийн сан (бүх өгөгдлийн төлөв) | Систем | CTO / DBA | Confidential | db container | 3 | 3 | 3 | Өндөр | Өндөр |
| 6 | Админ/privileged нэвтрэх мэдээлэл | Нууц | ISMS админ | Confidential | Odoo users / password store | 3 | 3 | 2 | Өндөр | Өндөр |
| 7 | Төлбөрийн гарцын API түлхүүр ба интеграцын secret-ууд | Нууц | Санхүүгийн захирал | Confidential | odoo.conf / env | 3 | 3 | 1 | Өндөр | Өндөр |
| 8 | Backup багц (pg_dump, filestore, config snapshot) | Өгөгдөл | CTO | Confidential | host volume + off-site | 3 | 3 | 2 | Өндөр | Өндөр |
| 9 | Хүргэлтийн түнш рүү явах өгөгдлийн урсгал (хаяг, утас) | Интерфейс | Логистикийн менежер | Confidential | API / CSV export | 3 | 2 | 1 | Өндөр | Дунд |
| 10 | Odoo тохиргоо (odoo.conf, RBAC бүлгүүд, record rules) | Тохиргоо | CTO | Internal | git / docker volume | 2 | 3 | 2 | Дунд | Дунд |
| 11 | Системийн лог ба audit trail (odoo.log, OCA auditlog, chatter) | Өгөгдөл | ISMS админ | Internal | /var/lib/odoo, DB | 2 | 3 | 1 | Дунд | Дунд |
| 12 | Ажилтны эрхийн бүртгэл (хэн, ямар бүлэг, хэзээ олгосон) | Баримт | HR менежер | Internal | Odoo Employees/Users | 2 | 3 | 1 | Дунд | Дунд |
| 13 | Ажилтны төхөөрөмж (хадгалсан session-тай laptop) | Төхөөрөмж | HR / IT | Internal | Оффис | 2 | 2 | 2 | Дунд | Дунд |
| 14 | Бүтээгдэхүүний каталоги ба үнэ | Өгөгдөл | Борлуулалтын захирал | Public | Odoo Products | 1 | 3 | 2 | Дунд | Дунд |

## Тайлбар

- **Хамгийн өндөр үнэтэй 6 хөрөнгө** (1,2,5,6,7,8) бүгд нууцлалын (Confidential) харьяат бөгөөд risk register-ийн High эрсдлүүд эдгээрт чиглэнэ.
- **Хөрөнгө систем биш** гэдэг зарчим: "Odoo ERP" гэж нэг мөр бичихийн оронд доторх өгөгдөл, нууц, тохиргоог тусад нь бүртгэв — эмнэлгийн жишээгээр "электрон систем" ≠ "өвчтөний регистр" (workbook discipline).
- Odoo дахь бүртгэл: мэдээллийн хөрөнгийг **Maintenance → Equipment** (систем/төхөөрөмж) болон **Inventory → Products** модуляар оруулсан; Documents Enterprise байхгүй тул энэ хослолыг сонгов.
