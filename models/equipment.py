from odoo import api, fields, models

TYPE = [
    ('head','Head'),
    ('foot','Foot'),
    ('hand','Hand')
]

class Equipment(models.Model):
    _name = "equipment"

    name = fields.Char(string="Name")
    type = fields.Selection(TYPE, string="type", default='NONE')
    weight = fields.Float(string="Weight")
    portable = fields.Boolean(string="Portable")

