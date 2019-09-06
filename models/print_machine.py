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

class PrintMachine(models.Model):

	_name = "print.machine"
	_description = 'Print Machine'
	_order = 'name'

	name = fields.Char(string="Print Machine", required=True)
	preparation_time = fields.Float(string="Preparation Time (Hours)")
	roller_width = fields.Float(string="Roller Width (Inches)")
	print_speed = fields.Float(string="Print Speed (Inches/min)", readonly=True, store=True) 


	_sql_constraints = [(u'print_machine_constraint_name', 'unique(name)', u'This printing machine already exists.')]


PrintMachine()