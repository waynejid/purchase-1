# -*- coding: utf-8 -*-
{
    'name': "Product Cost History",

    'summary': """
    """,

    'description': """
        Product Cost History
        
        Adds a view to display the cost history of a product
        
        This module has been developed by Jason PINDAT, intern @ AbAKUS it-solutions.
    """,

    'author': "Jason PINDAT, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '9.0.1.0',

    'depends': ['base', 'sale'],

    'data': [
        'views/product_price_history.xml',
        'views/product_product_button.xml'
    ],
}