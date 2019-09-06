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
#    Autor: Brayhan Andres Jaramillo Castaño
#    Correo: brayhanjaramillo@hotmail.com
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################


{
	'name': 'Print Labels',
	'category': 'Quoations',
	'version': '12.0',
	'author': 'Brayhan Andres Jaramillo Castaño' ,
	'license': 'LGPL-3',
	'maintainer': 'brayhanjaramillo@hotmail.com',
	'website': '',
	'summary': '',
	'images': [],

	'description': """

	Módulo test para pragmatic

	""",
	'depends': [ 'base'],

	'data': [
	
		'report/quoation_printing_label_report.xml',
		'security/ir.model.access.csv',
		'views/quoation_print_label_line_view.xml',
		'views/quoation_print_label_view.xml',
		'views/type_paper_view.xml',
		'views/print_machine_view.xml',
		'views/menu.xml',
		'data/data_sequence.xml',
		'views/res_partner_inherit_view.xml'

	],


	'installable': True,
	'application': True,
	'auto_install': False,


}


