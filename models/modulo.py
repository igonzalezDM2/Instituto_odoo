from odoo import models, fields

#REPRESENTA UN MÓDULO QUE IMPARTEN LOS TUTORES
class Modulo(models.Model):
    _name           = 'instituto.modulo'
    _description    = 'Modelo para representar un módulo'

    _rec_name = 'nombre'

    #Los campos del modelo
    nombre              = fields.Char(string='Nombre', required=True) #El nombre del módulo
    horas               = fields.Integer(string="Horas", required=False) #Su número reglamentario de horas
    tutores = fields.Many2many(comodel_name="instituto.tutoria_fct", relation="tutoria_fct_modulo_rel", column1="modulo_id", column2='tutor_id', string="Tutores") #Los tutores que imparten el módulo
