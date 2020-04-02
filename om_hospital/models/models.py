# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	additional_note = fields.Char(string='Additional Note')

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = 'mail.thread'
    _description = 'patient_data'
    _rec_name ="patient_name"

    @api.constrains('patient_age')
    def set_age(self):
    	for rec in self:
    		if rec.patient_age <=5:
    			raise ValidationError('You cannot have more than one account with')

# <!-- Adding chnage fields when the age is minor and major
    @api.depends('patient_age')
    def set_age_group(self):
    	for rec in self:
	    	if rec.patient_age:
	    		if rec.patient_age<18:
	    			rec.age_group ='minor'
	    		else:
	    			rec.age_group = 'major'

    # @api.multi
    # def appointment_open(self):
    #     return {
    #         'name': _('appointment'),
    #         'domain': [],
    #         'view_type': 'form',
    #         'res_model': 'hospital.appointment',
    #         'view_id': False,
    #         'view_mode': 'Tree,form',
    #         'type': 'ir.actions.act_window',
    #     }

    # def get_appointment_count(self):
    #     count = self.env[hospital.appointment].search_count(['patiet_id' ,'=', self.id ])
    #     self.appointment_count = count





    patient_name = fields.Char(string="Name", required=True, track_visibility="always")
    patient_age = fields.Integer(string="Age", track_visibility="always")
    note = fields.Text(string="Note")
    image = fields.Binary(string="Image")
    seq_id = fields.Char(string="Id")
    gender = fields.Selection([('male','Male'),('female','Female')]
    	,default="male", string="gender")
    age_group = fields.Selection([('major','major'),('minor','Minor')]
    	,string="age group", compute='set_age_group')
    appointment_count = fields.Char(string="Appointment Count")