# -*- coding: utf-8 -*-
{
    'name': "view_only_employee",

    'summary': """
        Habilita una casilla para indicar si un contacto es un empleado""",

    'description': """
        Cuando introduces un contacto en informacion personal dentro de un empleado, este pasa a ser visible por todos por que se crea un contacto
        con View Only Employee, se crea una casilla ¿Es empleado?, que si la marcas, hace que ese contaco solo sea visible por aquellos que sean officer dentro de recursos humanos.
    """,

    'author': "Tlaloc-ES",
    'website': "http://www.tlaloc-es.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'contacts',],

    # always loaded
    'data': [
        'templates.xml',
    ],

}