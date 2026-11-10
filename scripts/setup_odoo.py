#!/usr/bin/env python3
"""shoppy.mn ISMS demo configuration for Odoo 18 Community.

Idempotent-ish: run once on a fresh 'shoppy' DB. Uses XML-RPC.
"""
import xmlrpc.client

URL = "http://localhost:8069"
DB = "shoppy"
ADMIN = "admin"
PWD = "admin"

common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
uid = common.authenticate(DB, ADMIN, PWD, {})
assert uid, "auth failed"
models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")


def x(model, method, args, kwargs=None):
    return models.execute_kw(DB, uid, PWD, model, method, args, kwargs or {})


def find1(model, domain):
    ids = x(model, "search", [domain], {"limit": 1})
    return ids[0] if ids else None


print("== 1. Company ==")
co = find1("res.company", [])
x("res.company", "write", [[co], {
    "name": "Shoppy.mn LLC",
    "street": "Peace Avenue 15",
    "city": "Ulaanbaatar",
    "country_id": find1("res.country", [("code", "=", "MN")]),
    "email": "info@shoppy.mn",
    "website": "https://shoppy.mn",
}])
mnt = find1("res.currency", [("name", "=", "MNT")])
if mnt:
    x("res.currency", "write", [[mnt], {"active": True}])
    x("res.company", "write", [[co], {"currency_id": mnt}])
print("  company:", x("res.company", "read", [[co], ["name", "city", "country_id"]]))

print("== 2. RBAC groups ==")
cat = find1("ir.module.category", [("name", "=", "Uncategorized")]) or False


def grp(name, implied=None):
    g = find1("res.groups", [("name", "=", name)])
    if not g:
        g = x("res.groups", "create", [{
            "name": name, "category_id": cat,
            "implied_ids": [(6, 0, implied or [])],
        }])
    return g


def gid(xmlid):
    return x("ir.model.data", "search_read",
             [[["module", "=", xmlid.split(".")[0]], ["name", "=", xmlid.split(".")[1]]]],
             {"fields": ["res_id"], "limit": 1})[0]["res_id"]


g_isms = grp("Shoppy / ISMS Admin")
g_sales_mgr = gid("sales_team.group_sale_manager")
g_sales_own = gid("sales_team.group_sale_salesman")      # own docs only
g_stock = gid("stock.group_stock_user")
g_auditor = grp("Shoppy / Auditor")
g_project_user = gid("project.group_project_user")

print("  groups ok")

print("== 3. Auditor read-only access rules ==")
for model_name, name in [
    ("sale.order", "auditor_read_sale_order"),
    ("res.partner", "auditor_read_partner"),
    ("project.task", "auditor_read_task"),
    ("maintenance.equipment", "auditor_read_equipment"),
    ("stock.picking", "auditor_read_picking"),
    ("auditlog.log", "auditor_read_auditlog"),
    ("auditlog.rule", "auditor_read_auditrule"),
]:
    model_id = find1("ir.model", [("model", "=", model_name)])
    exists = find1("ir.model.access", [("name", "=", name)])
    if model_id and not exists:
        x("ir.model.access", "create", [{
            "name": name, "model_id": model_id, "group_id": g_auditor,
            "perm_read": 1, "perm_write": 0, "perm_create": 0, "perm_unlink": 0,
        }])
print("  auditor access ok")

print("== 4. Users ==")

def mkuser(name, login, groups):
    u = find1("res.users", [("login", "=", login)])
    grp_cmds = [(6, 0, groups)]
    if not u:
        u = x("res.users", "create", [{
            "name": name, "login": login, "password": "shoppy123",
            "groups_id": grp_cmds, "company_id": co, "company_ids": [(6, 0, [co])],
        }])
    else:
        x("res.users", "write", [[u], {"groups_id": grp_cmds}])
    return u


base_user = gid("base.group_user")
u_sm = mkuser("Batzorig Sales Manager", "salesmgr", [base_user, g_sales_mgr])
u_s1 = mkuser("Sarnai Sales", "sales1", [base_user, g_sales_own])
u_s2 = mkuser("Temuulen Sales", "sales2", [base_user, g_sales_own])
try:
    g_audit_user = gid("auditlog.group_auditlog_user")
except Exception:
    g_audit_user = None
u_wh = mkuser("Nyam Warehouse", "wh1", [base_user, g_stock])
u_au = mkuser("Oyun Auditor", "auditor1", [g for g in [base_user, g_auditor, g_project_user, g_audit_user] if g])
u_is = mkuser("Prost ISMS Admin", "isms", [base_user, g_isms, g_sales_mgr, g_project_user])
print("  users:", [x("res.users", "read", [[i], ["login"]])[0]["login"] for i in [u_sm, u_s1, u_s2, u_wh, u_au, u_is]])

print("== 5. Products + customers + orders ==")
for pname, price in [("Mongol Cashmere Scarf", 89000), ("Leather Boots", 250000),
                     ("Smart Watch X2", 450000), ("Gobi Wool Blanket", 120000)]:
    if not find1("product.product", [("name", "=", pname)]):
        x("product.product", "create", [{"name": pname, "list_price": price, "sale_ok": True}])

cust_ids = []
for cname, email in [("Bold Erdene", "bold@example.mn"), ("Sarnai Tuya", "sarnai@example.mn"),
                     ("Munkh Bat", "munkh@example.mn")]:
    c = find1("res.partner", [("name", "=", cname)])
    if not c:
        c = x("res.partner", "create", [{"name": cname, "email": email, "city": "Ulaanbaatar"}])
    cust_ids.append(c)

# orders: two owned by sales1, one by sales2  -> record-rule demo
prods = x("product.product", "search", [[["sale_ok", "=", True]]], {"limit": 4})
for owner, cust in [(u_s1, cust_ids[0]), (u_s1, cust_ids[1]), (u_s2, cust_ids[2])]:
    exists = x("sale.order", "search_count", [[["user_id", "=", owner], ["partner_id", "=", cust]]])
    if not exists:
        x("sale.order", "create", [{
            "partner_id": cust, "user_id": owner,
            "order_line": [(0, 0, {"product_id": p, "product_uom_qty": 1}) for p in prods[:2]],
        }])
print("  orders done")

print("== 6. Incident Response project ==")
sev_tags = {}
for t in ["severity-low", "severity-medium", "severity-high", "severity-critical"]:
    t_id = find1("project.tags", [("name", "=", t)])
    if not t_id:
        t_id = x("project.tags", "create", [{"name": t}])
    sev_tags[t] = t_id

def project_with_stages(pname, stage_names):
    p = find1("project.project", [("name", "=", pname)])
    if not p:
        p = x("project.project", "create", [{"name": pname, "privacy_visibility": "employees"}])
    for i, s in enumerate(stage_names):
        st = find1("project.task.type", [("name", "=", s), ("project_ids", "in", [p])])
        if not st:
            st = x("project.task.type", "create", [{"name": s, "sequence": i + 1, "project_ids": [(4, p)]}])
    return p

p_inc = project_with_stages("Incident Response",
                            ["Incident", "Report", "Investigate", "Resolve", "Close"])
inc_stage = find1("project.task.type", [("name", "=", "Investigate"), ("project_ids", "in", [p_inc])])
if not find1("project.task", [("name", "ilike", "phishing"), ("project_id", "=", p_inc)]):
    x("project.task", "create", [{
        "name": "Phishing test: 2 staff clicked simulation link",
        "project_id": p_inc, "stage_id": inc_stage,
        "tag_ids": [(4, sev_tags["severity-medium"])],
        "user_ids": [(4, u_is)],
        "description": "Simulated phishing campaign: 2/10 staff clicked. "
                       "Asset: staff credentials. Evidence: campaign report 2026-11. "
                       "Next: awareness training + MFA enforcement (R7).",
    }])
print("  incident project ok")

print("== 7. Risk Register project ==")
p_risk = project_with_stages("Risk Register",
                             ["Identified", "Analysed", "Treated", "Accepted"])
stg_ids = x("project.task.type", "search", [[["project_ids", "in", [p_risk]]]])
stages = {s["name"]: s["id"] for s in x("project.task.type", "read", [stg_ids], {"fields": ["name"]})}

RISKS = [
    ("R1 SQL injection on shop search", "I5xL3=15 High",
     "Threat: SQL injection via storefront input.\nVulnerability: weak input validation.\nWeakness found: staging scan showed search param reflected unescaped.\nTreatment: Mitigate - A.8.28, A.8.8, A.8.26. Owner: CTO.", "Treated"),
    ("R2 Admin access without MFA", "I4xL3=12 Med",
     "Threat: unauthorised admin login.\nVuln: MFA not enforced on all accounts.\nWeakness: access review found 3/8 accounts without MFA.\nTreatment: Mitigate - A.5.17, A.8.5, A.5.16. Owner: ISMS admin.", "Treated"),
    ("R3 Data loss - untested backups", "I5xL3=15 High",
     "Threat: unrecoverable data loss.\nVuln: no restore test ever run.\nWeakness: 12-month review shows zero restores; size-only checks.\nTreatment: Mitigate - A.8.13, A.5.29. Owner: CTO.", "Treated"),
    ("R4 Payment gateway API key exposure", "I4xL2=8 Med",
     "Threat: gateway secret leaked.\nVuln: key in plaintext odoo.conf.\nWeakness: config readable by docker group users.\nTreatment: Mitigate - A.8.24, A.5.17, A.8.9. Owner: CFO.", "Treated"),
    ("R5 Excess PII to delivery partner", "I4xL3=12 Med",
     "Threat: PII over-shared with third party.\nVuln: no need-to-know limit on export.\nWeakness: delivery CSV includes email + full order history.\nTreatment: Mitigate - A.5.34, A.5.14, A.5.20. Owner: Logistics mgr.", "Analysed"),
    ("R6 DDoS at promo peak", "I4xL3=12 Med",
     "Threat: DDoS/capacity outage on promo days.\nVuln: no rate limit/CDN/WAF.\nWeakness: load test degraded at 3x baseline.\nTreatment: Mitigate+Transfer - A.8.20, A.8.21, A.5.30. Owner: CTO.", "Analysed"),
    ("R7 Staff phishing credential loss", "I3xL4=12 Med",
     "Threat: phishing steals staff credentials.\nVuln: no training, single-factor.\nWeakness: simulation - 2/10 clicked.\nTreatment: Mitigate - A.6.3, A.8.5. Owner: HR.", "Treated"),
    ("R8 Insider order tampering", "I4xL3=12 Med",
     "Threat: insider modifies confirmed orders.\nVuln: all sales staff can edit any order, no approval step.\nWeakness: permission audit - no confirm workflow.\nTreatment: Mitigate - A.8.3, A.5.15, A.5.3. Owner: Sales dir.", "Treated"),
    ("R9 Unpatched CVEs on Odoo/host", "I4xL3=12 Med",
     "Threat: exploit of known CVEs.\nVuln: irregular patch cycle.\nWeakness: version check - Odoo 4 months behind; kernel CVEs open.\nTreatment: Mitigate - A.8.8, A.8.9. Owner: CTO.", "Treated"),
    ("R10 Lost laptop live session", "I3xL2=6 Low",
     "Threat: lost device gives live ERP session.\nVuln: no disk encryption, persistent browser session.\nWeakness: 2/5 laptops lack FDE.\nTreatment: Mitigate - A.8.1, A.5.17. Owner: IT admin.", "Accepted"),
    ("R11 Admin actions untraceable", "I3xL3=9 Med",
     "Threat: no accountability for admin changes.\nVuln: audit log disabled.\nWeakness: no record of who changed March sale prices.\nTreatment: Mitigate - A.8.15, A.8.16 (OCA auditlog). Owner: ISMS admin.", "Treated"),
    ("R12 Bulk export of customer list", "I4xL3=12 Med",
     "Threat: insider exfiltrates full customer list.\nVuln: bulk export enabled for all users.\nWeakness: UI check - any sales user can export all partners to CSV.\nTreatment: Mitigate - A.8.3, A.5.15. Owner: ISMS admin.", "Analysed"),
]
for rname, score, desc, stg in RISKS:
    if not find1("project.task", [("name", "=", rname), ("project_id", "=", p_risk)]):
        x("project.task", "create", [{
            "name": f"{rname} [{score}]", "project_id": p_risk,
            "stage_id": stages.get(stg), "description": desc,
            "user_ids": [(4, u_is)],
        }])
print("  risk register ok")

print("== 8. Maintenance assets (IT equipment / systems) ==")
ASSETS = [
    ("ASSET-01 Customer master data (res.partner)", "High"),
    ("ASSET-02 Order & payment records (sale.order)", "High"),
    ("ASSET-03 Web storefront (website_sale)", "High"),
    ("ASSET-04 Odoo ERP backend", "High"),
    ("ASSET-05 PostgreSQL database", "High"),
    ("ASSET-06 Admin credentials", "High"),
    ("ASSET-07 Payment gateway API keys", "High"),
    ("ASSET-08 Backup sets (pg_dump + filestore)", "High"),
    ("ASSET-09 Delivery partner data feed", "High"),
    ("ASSET-10 Odoo configuration (odoo.conf, RBAC)", "Medium"),
    ("ASSET-11 System logs & audit trail", "Medium"),
    ("ASSET-12 Staff access rights register", "Medium"),
]
cat_id = find1("maintenance.equipment.category", [])
for aname, crit in ASSETS:
    if not find1("maintenance.equipment", [("name", "=", aname)]):
        x("maintenance.equipment", "create", [{
            "name": aname, "category_id": cat_id,
            "note": f"shoppy.mn ISMS asset - criticality {crit} (see Asset Register doc 03)",
        }])
print("  assets ok")

print("== 9. OCA auditlog rules ==")
for m in ["res.partner", "sale.order"]:
    model_id = find1("ir.model", [("model", "=", m)])
    rule = find1("auditlog.rule", [("model_id", "=", model_id)])
    if model_id and not rule:
        x("auditlog.rule", "create", [{
            "name": f"ISMS log {m}", "model_id": model_id,
            "log_type": "full", "state": "subscribed",
            "log_read": False, "log_create": True, "log_write": True, "log_unlink": True,
        }])
    elif rule:
        x("auditlog.rule", "write", [[rule], {"state": "subscribed"}])
print("  auditlog ok")

print("DONE")
