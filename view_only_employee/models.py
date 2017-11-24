# -*- coding: utf-8 -*-
from openerp import models, fields, api

class view_only_employee(models.Model):
	_inherit = 'res.partner'
	isEmployee = fields.Boolean(string="¿Es empleado?")