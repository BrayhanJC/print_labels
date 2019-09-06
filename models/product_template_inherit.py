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

from odoo import api, fields, models, _
import time
from datetime import datetime, timedelta, date
import logging
_logger = logging.getLogger(__name__)
from odoo import modules
from odoo.addons import decimal_precision as dp

class ProductTemplateInherit(models.Model):



	_inherit = 'product.template'

	#type print
	TYPE_PRINT = [('digital', 'Digital'), ('flexographic', u'flexográfica')]

	quantity_inks = fields.Integer(string= "Quantity Inks", required=True)
	label_width = fields.Float(string= "Label Width (mm)", required=True)
	label_long = fields.Float(string= "Label Long (mm)", required=True)
	type_print = fields.Selection(TYPE_PRINT, string="Type Print")
	type_paper_id = fields.Many2one('type.paper', string="Type Paper", required=True)
	print_machine_id = fields.Many2one('print.machine', string="Printing Machine", required=True)
	waste_percentage = fields.Float(string="Waste Percentage", required=True)
	utility_percentage = fields.Float(string="Utility Percentage", required=True)
	value_hour_operator = fields.Float(string="Hour Operator", required=True)



	def calculate_cost(self):

		if self.type_print:

			cost_label=0

			if self.type_print == 'digital':

				cost_label = ((self.label_long * self.label_width) * 1 * self.type_paper_id.cost_paper) + (self.print_machine_id.preparation_time * self.value_hour_operator)


			if self.type_print == 'flexographic':

				cost_label = (((self.label_long * self.label_width) + (self.waste_percentage/100)) * 1 * self.type_paper_id.cost_paper) + ((self.print_machine_id.preparation_time * self.quantity_inks) * self.value_hour_operator) + (self.print_machine_id.preparation_time * self.value_hour_operator)

	
			return cost_label

		return 0


	def calculate_utility(self, standard_price):


		if self.utility_percentage:

			utility_total = standard_price * (self.utility_percentage / 100)
			 
			list_price = standard_price + utility_total

			return list_price

		return 0






	@api.model
	def create(self, vals):

		standard_price = self.calculate_cost()
		list_price = self.calculate_utility(standard_price)

		res = super(ProductTemplateInherit, self).create(vals)

		res.write({'standard_price': standard_price, 'list_price': list_price})


		return res

	@api.multi
	def write(self, vals):

		standard_price = self.calculate_cost()
		list_price = self.calculate_utility(standard_price)

		vals['standard_price'] = standard_price
		vals['list_price'] = list_price

		res = super(ProductTemplateInherit, self).write(vals)

		return res

ProductTemplateInherit()