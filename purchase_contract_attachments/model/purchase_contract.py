from openerp import models, fields

class purchaseContractWithAttachment(models.Model):
    _inherit = ['sale.subscription']
    
    attachments_ids = fields.Many2many('ir.attachment', string="Attachments")
