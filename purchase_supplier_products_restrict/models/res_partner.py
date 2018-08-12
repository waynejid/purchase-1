# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vendor_products_count = fields.Integer(compute='_compute_vendor_products_count')

    @api.one
    def _compute_vendor_products_count(self):
        self.vendor_products_count = self.env['product.template'].search_count([('seller_ids.name', '=', self.id)])
