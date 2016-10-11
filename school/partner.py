# -*- coding: utf-8 -*-
from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    eiec = fields.Boolean("电教馆", default=False)

    numberOfDevice = fields.Integer()
    subordinateSchool = fields.One2many('school.school','x_schoolName',readonly=True)