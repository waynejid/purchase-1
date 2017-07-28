# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

# import logging
# _logger = logging.getLogger(__name__)
    
    
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    price_history_count = fields.Integer(string="Price History Count", compute='_compute_price_history_count')
    
    @api.one
    def _compute_price_history_count(self):
        self.price_history_count = len(self.env['product.price.history'].search([('product_id.product_tmpl_id.id', '=', self.id)]))