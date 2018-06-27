# -*- coding: utf-8 -*-
{
    'name': "Purchase Supplier Crawler Available",
    'description': """
        Purchase Supplier Crawler Available
        
        - This module adds a check box in the supplier form to mark them as 'crawer available' for the Chrome Web App to select the correct suppliers

    This module has been developped by Valentin Thirion @ AbAKUS it-solutions
    """,

    'author': "AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Purchase',
    'version': '9.0.1.0',

    'depends': [
        'purchase',
    ],

    'data': [
        'views/supplier_view.xml',
    ],
}