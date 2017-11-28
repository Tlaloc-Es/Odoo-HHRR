# -*- coding: utf-8 -*-
from openerp import models, fields, api

class view_only_employee(models.Model):
	_inherit = 'res.partner'
	employeeID = fields.Many2one('hr.employee', ondelete='set null', string="Empleado", help='Indica a que empleado pertenece este contacto y lo oculta para todos los empleados.', index=True)
