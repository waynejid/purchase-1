# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    purchase_mode = fields.Selection([('email', 'Email'), ('fax', 'Fax'), ('paper', 'Paper'), ('phone', 'Phone'), ('webstore', 'Webstore')], string="Purchase Mode")
