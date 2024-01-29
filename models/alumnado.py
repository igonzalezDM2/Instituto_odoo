from odoo import api, fields, models

#Modelo que representa a un alumno
class Alumnado(models.Model):
    _name           = 'instituto.alumnado'
    _description    = 'Modelo para representar a los alumnos del instituto'

    #Enumerado de los ciclos formativos
    CICLOS = [
        ('DAM', 'Desarrollo Multiplataforma'),
        ('DAW', 'Desarrollo Web'),
        ('ASIR', 'Administración de Sistemas')
    ]
    _rec_name = 'nombre'

    #Los campos del modelo
    nombre              = fields.Char(string='Nombre', required=True)
    apellidos           = fields.Char(string='Apellidos', required=True)
    fecha_nacimiento    = fields.Date(string="Fecha nacimiento", required=True)
    direccion           = fields.Char(string="Dirección", required=False)
    codigo_postal       = fields.Char(string="Código postal", required=False)
    email               = fields.Char(string="Email", required=False)
    ciclo_formativo     = fields.Selection(string="Ciclo formativo", selection=CICLOS, required=False, default=CICLOS[0][0])
    coche               = fields.Boolean(string="¿Dispone de automóvil?")
    otros               = fields.Char(string="Comentarios y observaciones", required=False)
    nota_media          = fields.Float(string="Nota media",  required=False, default=5.0)
    nota_media_texto    = fields.Char(compute='_get_nota_texto', string="Nota media",  required=False, default="aprobado")
    empresa             = fields.Many2one(comodel_name="instituto.empresa", string="Empresa", required=False)
    tutor             = fields.Many2one(comodel_name="instituto.tutoria_fct", string="Tutor", required=False)

    #Función para valorar la nota en texto
    @api.depends('nota_media')
    def _get_nota_texto(self):
        ret = "suspendido"
        for record in self:
            if record.nota_media >= 5:
                ret = "aprobado"
            if record.nota_media >= 7:
                ret = "notable"
            if record.nota_media >= 9:
                ret = "sobresaliente"
            record.nota_media_texto = ret
