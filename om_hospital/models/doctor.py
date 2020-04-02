# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = 'mail.thread'
    _description = 'patient_data1'
    _rec_name ="related_user"
    _order = "id desc"


    related_user = fields.Many2one('res.users', string="Realated User", required=True)
    name = fields.Char(string="Name")
    gender = fields.Selection([('male','Male'),('female','Female')]
        ,default="male", string="gender")