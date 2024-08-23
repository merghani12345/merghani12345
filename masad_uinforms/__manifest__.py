{
    'name': 'Masad Uinform Module',
    'depends': ['base','hr','product'],
    'author': 'merghani elfaki - HQ',
    'description': """ This module keeps track of real estate and sells them via a bidding process.""",
    'data': [
             'security/unifor_security.xml',
             'security/ir.model.access.csv',
             'views/configuration_views.xml',
             'views/uinform_employee.xml',
             'views/uinforms_menus.xml',
            'report/real_estate_report_views.xml',
            'report/real_estate_report_templates.xml',



             ],

    # ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
