# -*- coding: utf-8 -*-
{
    'name': 'Real Estate Allotment',
    'version': '18.0.1.0.0',
    'category': 'Real Estate',
    'summary': 'Allot client to project flats',
    'description': 'Allot client to project flats',
    'author': 'Real Estate ERP',
    'license': 'LGPL-3',
    'depends': ['real_estate_project', 'real_estate_partner', 'mail'],
    'data': ['security/ir.model.access.csv', 'views/re_allotment_views.xml', 'views/menu.xml'],
    'application': False,
    'installable': True,
}
