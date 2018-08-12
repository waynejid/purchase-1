# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
{
    'name': "Product Cost History",
    'version': '10.0.1.0.0',
    'author': "AbAKUS it-solutions SARL",
    'license': 'AGPL-3',
    'website': "http://www.abakusitsolutions.eu",
    'depends': [
        'base',
        'purchase'
    ],
    'category': 'Product',
    'data': [
        'views/product_template.xml',
        'views/product_cost_history.xml',
        'security/ir.model.access.csv'
    ],
}
