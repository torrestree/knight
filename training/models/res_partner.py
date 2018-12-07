from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit='res.partner'
    
    is_teacher=fields.Boolean(string='teacher')
    is_student=fields.Boolean(string='student')