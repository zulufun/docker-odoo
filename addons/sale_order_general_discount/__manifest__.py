
{
    "name": "Sale Order General Discount",
    "summary": "General discount per sale order",
    "version": "16.0.1.1.0",
    "development_status": "Production/Stable",
    "category": "Sales",
    "website": "https://github.com/zulufun/docker-odoo",
    "author": "Đỗ Đức Phúc - MMT&TTDL k56",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["sale"],
    "data": ["views/sale_order_view.xml", "views/res_partner_view.xml"],
    "images": ["static/description/icon1.png"],
}
