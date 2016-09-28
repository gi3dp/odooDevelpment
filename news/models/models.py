# -*- coding: utf-8 -*-

from openerp import models, fields, api

class News(models.Model):
    _name = 'news.news'

    title = fields.Char(required=True,string="标题")
    _create_date = fields.Date(string="发布日期",required=True)
    website = fields.Char(string="详细网址",required=True)
    source_id = fields.Many2one('news.website',string="来源",required=True)
    categorization = fields.Selection([('wechat','微信'),('weibo','微博'),
                                       ('video','视频'),('outer_news','外部新闻'),('inner_news','内部新闻')],
                                      default = 'outer_news')

class Website(models.Model):
    _name = 'news.website'

    name = fields.Char(string="源网站简称")
    source_site_link = fields.Char(string="源网站网址")


#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100