# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
from odoo import models, fields, api


class PurchaseOrderForm(models.Model):
    _inherit = ['purchase.order']

    export_csv = fields.Text()

    @api.multi
    def create_export_csv(self):
        purchase_order_line_obj = self.env['purchase.order.line']
        purchase_order_lines = purchase_order_line_obj.search([('order_id', '=', self.id)])
        if purchase_order_lines:
            text = ""
            for purchase_order_line in purchase_order_line_obj.browse(purchase_order_lines):
                reference = "NO REFERENCE"

                # get the supplier ref code
                supplierinfo_obj = self.env['product.supplierinfo']
                suppliers = supplierinfo_obj.search([
                    ('product_tmpl_id', '=', purchase_order_line.product_id.product_tmpl_id.id)])
                for supp in supplierinfo_obj.browse(suppliers):
                    if supp.name == self.partner_id:
                        reference = supp.product_code

                if reference == "NO REFERENCE" and purchase_order_line.product_id.code:
                    reference = purchase_order_line.product_id.code

                text += str(reference) + ", " + str(int(purchase_order_line.product_qty)) + "\r\n"

            if self.export_csv != text:
                self.export_csv = text
        else:
            if self.export_csv != "":
                self.export_csv = ""
