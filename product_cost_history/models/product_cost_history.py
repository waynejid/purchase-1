# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class ProductCostHistory(models.Model):
    _name = 'product.cost.history'
    _description = 'Product Cost History'
    _order = 'create_date desc'

    cost = fields.Float()
    product_id = fields.Many2one('product.product', string="Product")
