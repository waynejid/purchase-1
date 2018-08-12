# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    price_history_count = fields.Integer(compute='_compute_price_history_count')
    cost_price_last_update_text = fields.Char(string="Last Cost Price Update",
                                              compute='_compute_cost_price_last_update')

    @api.one
    def _compute_price_history_count(self):
        self.price_history_count = self.env['product.price.history'].search_count([
            ('product_id.product_tmpl_id.id', '=', self.id)
        ])

    @api.one
    def _compute_cost_price_last_update(self):
        history_ids = self.env['product.price.history'].search([
            ('product_id.product_tmpl_id.id', '=', self.id)], order='datetime DESC', limit=1)
        if len(history_ids) == 0:
            self.cost_price_last_update_text = str("Never")
        else:
            self.cost_price_last_update_text = str(history_ids.datetime)
