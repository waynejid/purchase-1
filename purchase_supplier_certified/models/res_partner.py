# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class CertifiedSupplier(models.Model):
    _inherit = 'res.partner'

    supplier_certified = fields.Boolean(string="Certified Supplier", default=False)
