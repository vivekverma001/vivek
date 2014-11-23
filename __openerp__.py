# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# {
#     "name" : "Project Budgeting",
#     "version" : "1.0",
#     "author" : "Ricky Verma",
#     "category" : "Project Management",
#     "website" : " ",
#     "description": """
#     This Module is to Budget the Project
#     """,
#     "depends" : ['web','project','account'],
#     "data":['project_budgeting_view.xml',
#             'security/ir.model.access.csv', ],
#     "js":[ ],
#     "qweb" : [],
#     'installable': True,
#     'auto_install': False,
# }

{
    'name': 'Project Budget',
    'version': '1.1',
    'author': 'OpenERP SA',
    'website': 'http://www.openerp.com',
    'category': 'Project Management',
    'sequence': 8,
    'summary': 'Projects, Tasks',
    'images': [
    ],
    'depends': [
        'base_setup',
        'product',
        'analytic',
        'board',
        'mail',
        'resource',
        'web_kanban'
    ],
    'description': """
Test
    """,
    'data': [
    ],
    'demo': [],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:


