from openerp import models, fields, api, _
import datetime
from datetime import date
import logging
_logger = logging.getLogger(__name__)

class product_wth_order_scheduled_date(models.Model):
    _inherit = ['product.product']

    next_expected_delivery_date = fields.Date(string="Next requested delivery date", compute="_compute_next_expected_delivery_date")
    supplier_to_reorder = fields.Char(string="Supplier", compute="_compute_supplier_name")

    @api.one
    @api.depends('virtual_available')
    def _compute_next_expected_delivery_date(self):
        if self.virtual_available < 0:
            # get the expected date on the oldest non complete stock.move for this product and set it to this product
            date_requested = 0

            moves_obj = self.pool.get('stock.move')
            moves = moves_obj.search(self.env.cr, self.env.uid, [['product_id', '=', self.id], ['state', 'not in', ('draft', 'cancel', 'done')], ['picking_id', 'like', 'OUT']], order="date_expected asc")

            for move in moves_obj.browse(self.env.cr, self.env.uid, moves):
                # get the sales order and get the requested date if set
                sale_order_number = move.origin
                sale_orders_obj = self.pool.get('sale.order')
                sale_orders = sale_orders_obj.search(self.env.cr, self.env.uid, [['name', '=', sale_order_number]])

                if len(sale_orders) == 1:
                    sale_orders = sale_orders_obj.browse(self.env.cr, self.env.uid, sale_orders)
                    sale_order = sale_orders[0]
                    if sale_order.requested_date != "":
                        # test if requested date is set
                        if date_requested == 0:
                            date_requested = sale_order.requested_date
                        # if sooner, take this date
                        else:
                            if sale_order.requested_date < date_requested:
                                date_requested = sale_order.requested_date

                # set the date
                self.next_expected_delivery_date = date_requested

    @api.one
    def _compute_supplier_name(self):
        if len(self.seller_ids) > 1:
            self.supplier_to_reorder = self.seller_ids[0].name.name
                
    @api.multi
    def reorder_product(self):
        qty_to_reorder = - self.virtual_available
        # get the first supplier and set this product to be ordered
        if len(self.seller_ids) < 1:
            raise osv.except_osv(_("Error"), _("No supplier set on this product.\nImpossible to re-order."))
        default_supplier = self.seller_ids[0].name.id

        # check if draft RFQ for this supplier
        requests_for_quotation_obj = self.pool.get('purchase.order')
        requests_for_quotation = requests_for_quotation_obj.search(self.env.cr, self.env.uid, [['partner_id', '=', default_supplier], ['state', 'in', ('draft', 'sent')]], order="date_order asc")

        rfq = None
        if len(requests_for_quotation) > 0:
            rfq = requests_for_quotation_obj.browse(self.env.cr, self.env.uid, requests_for_quotation)
            rfq = rfq[0]

        # If exists, check if a line exists with the quantity
        if rfq != None:
            line_exists = False

            for line in rfq.order_line:
                if line.product_id == self.id:
                    _logger.debug("\n\line exists for: %s", self.name)

                    # Line exists, check the quantity
                    #if line.product_qty < qty_to_reorder:
                    line.product_qty = line.product_qty + qty_to_reorder
                    line_exists = True
                    #else:

            if line_exists == False:
                _logger.debug("\n\line does not exist for: %s", self.name)

                # Line does not exist, create it
                self.pool.get('purchase.order.line').create(self.env.cr, self.env.uid, {
                    'order_id': rfq.id,
                    'product_id': self.id,
                    'product_template': self.product_tmpl_id.id,
                    'product_qty': qty_to_reorder,
                    'price_unit': self.seller_ids[0].pricelist_ids[0].price,
                    'date_planned': self.next_expected_delivery_date,
                    'taxes_id': self.supplier_taxes_id,
                })

        # RFQ does not exist, create it
        else:
            
            _logger.debug("\n\create purchase order for: %s", self.name)
            
        

    
