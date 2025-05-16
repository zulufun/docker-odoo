from lxml import etree
from odoo import api, fields, models
class SaleOrder(models.Model):
    _inherit = "sale.order"
    general_discount = fields.Float(
        string="Discount (%)",
        compute="_compute_general_discount",
        store=True,
        readonly=False,
        digits="Discount",
    )
    @api.depends("partner_id")
    def _compute_general_discount(self):
        for so in self:
            so.general_discount = so.partner_id.sale_discount
    @api.model
    def get_view(self, view_id=None, view_type="form", **options):
        res = super().get_view(view_id=view_id, view_type=view_type, **options)
        if view_type == "form":
            order_xml = etree.XML(res["arch"])
            order_line_fields = order_xml.xpath("//field[@name='order_line']")
            if order_line_fields:
                order_line_field = order_line_fields[0]
                context = order_line_field.attrib.get("context", "{}").replace(
                    "{",
                    "{'default_discount': general_discount, ",
                    1,
                )
                order_line_field.attrib["context"] = context
                res["arch"] = etree.tostring(order_xml)
        return res
