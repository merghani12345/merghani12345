# -*- coding: utf-8 -*-
# from odoo import http


# class MasadAssociation(http.Controller):
#     @http.route('/masad_association/masad_association', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/masad_association/masad_association/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('masad_association.listing', {
#             'root': '/masad_association/masad_association',
#             'objects': http.request.env['masad_association.masad_association'].search([]),
#         })

#     @http.route('/masad_association/masad_association/objects/<model("masad_association.masad_association"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('masad_association.object', {
#             'object': obj
#         })
