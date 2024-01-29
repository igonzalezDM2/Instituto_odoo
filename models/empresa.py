from odoo import models, fields

#Modelo que representa una empresa
class Empresa(models.Model):
    _name           = 'instituto.empresa'
    _description    = 'Modelo para representar una empresa'

    #Enumerado para los diferentes departamentos de la empresa
    DPTO = [
        ('INFORMATICA', 'Informática'),
        ('COMERCIO', 'Comercio'),
        ('MARKETING', 'Mercadotecnia'),
        ('ADMIN', 'Administración')
    ]

    _rec_name = 'nombre'

    #Los campos del modelo
    nombre              = fields.Char(string='Nombre', required=True)
    direccion           = fields.Char(string="Dirección", required=False)
    telefono            = fields.Char(string='Teléfono', required=False)
    departamento        = fields.Selection(string="Departamento", selection=DPTO, required=False, default=DPTO[0][0])
    alumnado            = fields.One2many(comodel_name="instituto.alumnado", inverse_name="empresa", string="Alumnos", required=False, )
