from odoo import models, fields

class Venta(models.Model):
    _name = 'ventas.venta'
    _description = 'Ventas externas'
    _table = 'ventas'  
    _auto = False  

    id = fields.Integer(string='ID', readonly=True)
    fecha = fields.Date(string='Fecha')
    cliente = fields.Char(string='Cliente')
    producto = fields.Char(string='Producto')
    cantidad = fields.Integer(string='Cantidad')
    precio_unitario = fields.Float(string='Precio Unitario')
    total = fields.Float(string='Total')
