# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
{
    'name': "BU for Purchases",
    'version': '10.0.1.0.0',
    'author': "AbAKUS it-solutions SARL",
    'license': 'AGPL-3',
    'depends': [
        'base',
        'purchase',
    ],
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Purchase',
    'data': [
        'data/ir_rule.xml',

        'views/purchase_order.xml',
    ],
    'installable': True,
    'application': False,
}
