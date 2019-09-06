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

class QuoationPrintLabel(models.Model):

	_name = "quoation.print_label"
	_description = 'Label Printing'
	_order = 'name'

	name = fields.Char(string="Quoation")
	partner_id = fields.Many2one('res.partner', string="Partner")
	print_label_line_ids = fields.One2many('quoation.print_label_line', 'print_label_id', string="Print Labels")
	total = fields.Float(string="Total")

	@api.onchange('print_label_line_ids')
	def onchange_print_label_line_ids(self):
		if self.print_label_line_ids:
			total = 0
			for x in self.print_label_line_ids:
				total += x.total


			self.total = total 

	@api.model
	def create(self, vals):
		_logger.info('sdfsfds')
		#if vals.get('name'):
		vals['name'] = self.env['ir.sequence'].next_by_code('quoation.print_label')
		res = super(QuoationPrintLabel, self).create(vals)
		return res
		


QuoationPrintLabel()