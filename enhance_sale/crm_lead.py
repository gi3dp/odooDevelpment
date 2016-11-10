# -*- coding:utf-8 -*-
from odoo import fields,models,api


class EnhanceCrmLead(models.Model):
    # 从crm.lead继承
    _inherit = 'crm.lead'

    #增加三个原本没有的字段todo:website从联系人引用
    registteredCaption = fields.Integer(string=u"注册资金(万)")
    mainBusiness = fields.Text( u"主营业务")
    website = fields.Char(string = u"网址")

    #根据注册资金修改评级
    @api.onchange('registteredCaption')
    def _onchange_priority(self):
        if self.registteredCaption > 500:
            self.priority = '3'
        if self.registteredCaption > 200 and  self.registteredCaption <= 500 :
            self.priority = '2'
        if self.registteredCaption <= 50:
            self.priority = '1'

    #为title设置默认值，未实现
    @api.one
    def _set_default_title(self):
        self.title = u'法人'

