# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class licee_8(models.Model):
#     _name = 'licee_8.licee_8'
#     _description = 'licee_8.licee_8'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100