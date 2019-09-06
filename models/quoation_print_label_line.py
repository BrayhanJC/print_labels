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

class QuoationPrintLabelLine(models.Model):

	_name = "quoation.print_label_line"
	_description = 'Quoation Print Label'
	_rec_name= 'print_label_id'
	_order = 'print_label_id'


	#type print
	TYPE_PRINT = [('digital', 'Digital'), ('flexographic', u'flexográfica')]
	partner_id = fields.Many2one('res.partner', string="Operator")
	print_label_id = fields.Many2one('quoation.print_label', string="Print Label")
	quantity_inks = fields.Integer(string= "Quantity Inks")
	quantity_labels = fields.Integer(string= "Quantity Labels")
	label_width = fields.Float(string= "Label Width")
	label_long = fields.Float(string= "Label Long")
	type_print = fields.Selection(TYPE_PRINT, string="Type Print")
	type_paper_id = fields.Many2one('type.paper', string="Type Paper")
	print_machine_id = fields.Many2one('print.machine', string="Printing Machine")
	waste_percentage = fields.Float(string="Waste Percentage")
	total = fields.Float(string="Total")



	@api.onchange('quantity_labels')
	def calculate_area(self):
		if self.type_print:

			_logger.info('entrando')

			if self.quantity_labels:

				cost_label=0

				if self.type_print == 'digital':

					cost_label = ((self.label_long * self.label_width) * self.quantity_labels * self.type_paper_id.cost_paper) + (self.print_machine_id.preparation_time * self.partner_id.value_hour)

				if self.type_print == 'flexographic':

					cost_label = (((self.label_long * self.label_width) + self.waste_percentage) * self.quantity_labels * self.type_paper_id.cost_paper) + ((self.print_machine_id.preparation_time * self.quantity_inks) * self.partner_id.value_hour) + (self.print_machine_id.preparation_time * self.partner_id.value_hour)

				self.total = cost_label


			
QuoationPrintLabelLine()