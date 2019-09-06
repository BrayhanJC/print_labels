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

class SaleOrderInherit(models.Model):

	_inherit = 'sale.order.line'

	@api.multi
	@api.depends('product_id', 'product_uom_qty')
	def _compute_total_cost(self):

		total_cost = 0
		for x in self:
			total_cost = x.product_id.standard_price * x.product_uom_qty

			x.total_cost = total_cost


	total_cost = fields.Monetary(compute='_compute_total_cost', string='Total Cost', store=True)
	label_width = fields.Float(string= "Label Width (mm)", related="product_id.label_width")
	label_long = fields.Float(string= "Label Long (mm)", related="product_id.label_long")
	quantity_inks = fields.Integer(string= "Quantity Inks", related="product_id.quantity_inks")



SaleOrderInherit()