# -*- coding: utf-8 -*-
{
    'name': 'Real Estate Payment Collection',
    'version': '18.0.1.0.0',
    'category': 'Real Estate',
    'summary': 'Payment submission form + approval workflow',
    'description': 'Payment submission form + approval workflow',
    'author': 'Real Estate ERP',
    'license': 'LGPL-3',
    'depends': ['real_estate_installment', 'account', 'mail'],
    'data': ['security/ir.model.access.csv', 'views/re_payment_submission_views.xml', 'views/menu.xml'],
    'application': False,
    'installable': True,
}
