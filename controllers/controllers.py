# -*- coding: utf-8 -*-
# from odoo import http


# class Konterhp(http.Controller):
#     @http.route('/konterhp/konterhp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/konterhp/konterhp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('konterhp.listing', {
#             'root': '/konterhp/konterhp',
#             'objects': http.request.env['konterhp.konterhp'].search([]),
#         })

#     @http.route('/konterhp/konterhp/objects/<model("konterhp.konterhp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('konterhp.object', {
#             'object': obj
#         })
