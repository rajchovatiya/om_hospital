# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ResPartners(models.Model):
    _inherit = 'res.partner'

#override the create function whn click on custmor create button that time call this function
    @api.model
    def create(self , vals_list):
        # import pdb; pdb.set_trace()
        res = super(ResPartners, self).create(vals_list)
        print("this function is working")
        return res


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

# state widget button onclik drat to confirm button
    @api.multi
    def action_confirm(self):
        for so in self:
            so.state="confirm"
    @api.multi
    def action_done(self):
        for so in self:
            so.state="done"