# -*- coding: utf-8 -*-
from odoo import http

# class EnhanceSale(http.Controller):
#     @http.route('/enhance_sale/enhance_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/enhance_sale/enhance_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('enhance_sale.listing', {
#             'root': '/enhance_sale/enhance_sale',
#             'objects': http.request.env['enhance_sale.enhance_sale'].search([]),
#         })

#     @http.route('/enhance_sale/enhance_sale/objects/<model("enhance_sale.enhance_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('enhance_sale.object', {
#             'object': obj
#         })