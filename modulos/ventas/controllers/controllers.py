# from odoo import http
# from odoo.http import request

# class Ventas(http.Controller):

#     @http.route('/ventas', auth='public', website=True)
#     def listado(self, **kw):
#         ventas = request.env['ventas.venta'].sudo().search([])
#         return request.render('ventas_extra.ventas_venta_listing', {
#             'ventas': ventas,
#             'root': '/ventas',
#         })

#     @http.route('/ventas/<int:venta_id>', auth='public', website=True)
#     def detalle(self, venta_id, **kw):
#         venta = request.env['ventas.venta'].sudo().browse(venta_id)
#         if not venta.exists():
#             return request.not_found()
#         return request.render('ventas_extra.ventas_venta_detail', {
#             'venta': venta
#         })
