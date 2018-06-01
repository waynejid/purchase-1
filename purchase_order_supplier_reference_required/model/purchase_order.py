from openerp import models, fields

class account_asset_asset_complete_annuity(models.Model):
    _inherit = 'purchase.order'

    partner_ref = fields.Char(required=True)
