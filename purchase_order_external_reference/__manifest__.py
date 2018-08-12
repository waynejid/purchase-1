# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
{
    'name': "Purchase Order External Reference",
    'version': '10.0.1.0.0',
    'author': "AbAKUS it-solutions SARL",
    'license': 'AGPL-3',
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Product',
    'depends': [
        'base',
        'purchase',
        'partner_reference_external',
    ],
    'data': [
        'views/purchase_order.xml',
        'reports/purchase_order_reports.xml',
    ],
}
