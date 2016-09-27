# -*- coding: utf-8 -*-

from openerp import models, fields, api

class School(models.Model):
    _name = 'school.school'


    x_checkCondition = fields.Boolean(string="验收情况")
    x_checkCertificationNumber = fields.Integer(string="验收单张数")

    x_schoolName = fields.Char(required=False, string="学校名称")
    x_phoneNumber = fields.Char(string="电话")

    x_trainingteacher = fields.Char(string="培训老师")
    x_receptionData = fields.Date(string="接收日期")
    x_contact2= fields.Char(string="联系人2")
    x_phoneNumber2 = fields.Char(string="电话2")
    x_remark = fields.Char(string="备注")
    x_city = fields.Char(required=False, string="市，州")
    x_town = fields.Char(required=False, string="县区")
    x_QQ = fields.Char(required=False, string="QQ号")
    x_mail = fields.Char(string="邮箱地址")
    x_equipmentNumber = fields.Integer(required=False, string="设备套数")
    x_schoolAddress = fields.Char(required=False, string="学校地址")
    x_Name = fields.Char(required=False, string="联系人")
    x_contractPhoneNumber = fields.Char(required=False, string="联系人电话(座机或手机)")
