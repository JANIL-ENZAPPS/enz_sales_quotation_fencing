{
    'name': 'Enzapps Sales Quotation Fencing',
    'version': '16.0.1.1.0',
    'category': 'Sales Management',
    'summary': "Additional Sales Quotation Formate",
    'author': 'Enzapps Private Limited',
    'company': 'Enzapps Private Limited',
    'website': 'http://www.enzapps.com',
    'description': """

Additional Sales Quotation Formate With Discount
""",
    'depends': ['sale',
                'account','sale_discount_total','enz_multi_branch','enztrading','enz_trading_extension','enz_field_installation','enz_service_extenstion'
                ],
    'data': [
        'security/ir.model.access.csv',
        'reports/paper_format.xml',
        'reports/reports.xml',
        'reports/header.xml',
        'reports/fencing_view.xml',
        'views/sale_order.xml',
        'views/sale_report_format_details.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
}