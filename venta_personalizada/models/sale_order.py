from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    observacion_ingenieria = fields.Text(string='Observaciones de Ingeniería')
