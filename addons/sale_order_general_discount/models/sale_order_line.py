from odoo import api, models
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends("order_id", "order_id.general_discount")
    def _compute_discount(self):
        res = super()._compute_discount()
        for line in self:
            # kiểm tra giá trị của general_discount trên origin để bao gồm
            # trường hợp chiết khấu được đặt thành giá trị != 0 và sau đó
            # đặt lại thành 0 để xóa chiết khấu trên tất cả các dòng cùng một lúc
            if line.order_id.general_discount or line.order_id._origin.general_discount:
                line.discount = line.order_id.general_discount
        return res
