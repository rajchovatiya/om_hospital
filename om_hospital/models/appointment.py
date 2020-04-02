# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = 'mail.thread'
    _description = 'patient_data1'
    _rec_name ="patient_id"
    _order = "id desc"


    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    patient_age = fields.Integer(string="Age",related="patient_id.patient_age")
    note = fields.Text(string="Note")
    appointment_date = fields.Date(string="Date" , required=True)
    state = fields.Selection([('draft','Draft'),
					    	  ('confirm','Confirm'),
					    	  ('done','Done'),
					    	  ('cancle','Cancle')],string="status", default="draft")
    doctor_note = fields.Text(string="Note")
    pharmacy_note = fields.Text(string="NOte")
    @api.multi
    def action_confirm(self):
        for so in self:
            so.state="confirm"
    @api.multi
    def action_done(self):
        for so in self:
            so.state="done"