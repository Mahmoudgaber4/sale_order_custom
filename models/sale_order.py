from odoo import models, fields
from odoo .exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    check = fields.Boolean()
    unit_check = fields.Date()
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('confirm', 'Unit Confirm'),
        ('sale', 'Sales Order'),
        ('cancel', 'Cancelled'),
    ], default="draft")

    def change_unit(self):
        for rec in self:
            if rec.unit_check > rec.validity_date:
                raise ValidationError("Date of order is Expired")
            else:
                rec.state = "confirm"
    