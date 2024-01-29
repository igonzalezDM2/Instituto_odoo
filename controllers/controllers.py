# -*- coding: utf-8 -*-
# from odoo import http


# class Licee9(http.Controller):
#     @http.route('/licee_9/licee_9', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/licee_9/licee_9/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('licee_9.listing', {
#             'root': '/licee_9/licee_9',
#             'objects': http.request.env['licee_9.licee_9'].search([]),
#         })

#     @http.route('/licee_9/licee_9/objects/<model("licee_9.licee_9"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('licee_9.object', {
#             'object': obj
#         })
