{
    'name': "Product Re-Order Scheduled Date",
    'version': '9.0.1.0',
    'depends': ['sale', 'stock', 'sale_order_dates'],
    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sale',
    'description': 
    """
This modules adds a tree view in purchase for products that need to be reordered based on their virtual available quantity and next expected delivery date.

This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,
    'data': [
        'view/product_view.xml',
    ],
}
