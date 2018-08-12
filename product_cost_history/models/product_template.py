# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    cost_history_count = fields.Integer(compute='_compute_cost_history_count')

    @api.one
    def _compute_cost_history_count(self):
        self.cost_history_count = self.env['product.cost.history'].search_count([
            ('product_id.product_tmpl_id.id', '=', self.id)
        ])
