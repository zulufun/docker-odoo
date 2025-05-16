
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    attached_product_ids = fields.Many2many(
        comodel_name="product.product",
        relation="product_attached_rel",
        string="Đính kèm sản phẩm",
        help="Tương tự như các sản phẩm tùy chọn, tuy nhiên chúng được tự động "
        "thêm vào đơn bán hàng và có thể bị xóa khi sản phẩm chính bị xóa.",
    )
