# -*- coding: utf-8 -*-
{
    'name': "Hospital Maagement",
    'summary': "thx",       
    'description': "Hospital details",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','mail','sale'],
    'data': [
        'data/sequence.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/appointment.xml'
    ],
    # only loaded in demonstration mode
    #added
    'demo': [
        'demo/demo.xml',
    ],
}