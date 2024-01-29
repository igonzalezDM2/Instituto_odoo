from odoo import models, fields

#Modelo que representa un tutor de FCT
class TutoriaFCT(models.Model):
    _name           = 'instituto.tutoria_fct'
    _description    = 'Modelo para representar un tutor de FCT'

    _rec_name = 'nombre'

    #Los campos del modelo
    nombre              = fields.Char(string='Nombre', required=True)
    apellidos           = fields.Char(string='Apellidos', required=True)
    email = fields.Char(string="Email", required=True)
    direccion           = fields.Char(string="Dirección", required=False)
    codigo_postal       = fields.Char(string="Código postal", required=False)
    alumnado = fields.One2many(comodel_name="instituto.alumnado", inverse_name="tutor", string="Alumnos", required=False, )
    modulos = fields.Many2many(comodel_name="instituto.modulo", relation="tutoria_fct_modulo_rel", column1="tutor_id", column2='modulo_id', string="Módulos")
