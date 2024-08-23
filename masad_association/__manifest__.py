# -*- coding: utf-8 -*-
{
    'name': "نظام الدعم المجتمعي",

    'summary': """سجلات طلبات الدعم""",
    'sequence': -20,
    'description': """ نظام طلب الدعومات""",

    'author': "Defence Industries System",
    'website': "https://masad-sudan.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'الدعم المجتمعي',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/catgsp.xml',
        'views/sequence.xml',
        'views/templates.xml',
        'views/filter.xml',
        'report/report_assocition.xml_views.xml',
        'report/report_assocition_template.xml',
        'report/report_assocition_template2.xml',
        'report/report_assocition_template4.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,

}
