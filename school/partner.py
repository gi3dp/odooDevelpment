# -*- coding: utf-8 -*-
from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_eiec = fields.Boolean("是电教馆", default=False)
    is_school = fields.Boolean("是学校", default=False)

    numberOfDevice = fields.Integer()
    subordinateSchool = fields.One2many('school.school','eiec_id',readonly=True)

    test3Dtaoshu = fields.Integer()
    testPLA = fields.Integer()