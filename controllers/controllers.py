# -*- coding: utf-8 -*-
from odoo import http

# class NewOvertime(http.Controller):
#     @http.route('/new_overtime/new_overtime/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_overtime/new_overtime/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_overtime.listing', {
#             'root': '/new_overtime/new_overtime',
#             'objects': http.request.env['new_overtime.new_overtime'].search([]),
#         })

#     @http.route('/new_overtime/new_overtime/objects/<model("new_overtime.new_overtime"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_overtime.object', {
#             'object': obj
#         })