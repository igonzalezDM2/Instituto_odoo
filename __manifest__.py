# -*- coding: utf-8 -*-
{
    'name': 'Instituto',
    'summary': 'Gestión de FCT',
    'description': 'Módulo de gestión de los alumnos y tutores de FCT de un instituto.',
    'version': '1.1.0',
    'category': 'Human Resources',
    'author': 'Mr. González',
    'data': [
        'security/groups.xml',
        #'security/ir.model.access.csv',
        'views/menu_principal.xml',

        'views/alumnado/view_form.xml',
        'views/alumnado/view_tree.xml',
        'views/alumnado/menu.xml',

        'views/empresa/view_form.xml',
        'views/empresa/view_tree.xml',
        'views/empresa/menu.xml',

        'views/tutoria_fct/view_form.xml',
        'views/tutoria_fct/view_tree.xml',
        'views/tutoria_fct/menu.xml',

        'views/modulo/view_form.xml',
        'views/modulo/view_tree.xml',
        'views/modulo/view_kanban.xml',
        'views/modulo/menu.xml',
        #'views/web/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
