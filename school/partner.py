# -*- coding: utf-8 -*-
from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_eiec = fields.Boolean("是电教馆", default=False)
    is_school = fields.Boolean("是学校", default=False)

    numberOfDevice = fields.Integer(string="设备数量")
    subordinateSchool = fields.One2many('school.school','eiec_id',readonly=True,
                                        string="下属学校")

    test3Dtaoshu = fields.Integer(string="3d设备套数")
    testPLA = fields.Integer(string="线材购买数量")