# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    crawler_available = fields.Boolean(default=False,
                                       help="Check this box if the ChromeWeb App is available for this supplier")
