#-*- coding: utf-8 -*-
import selectors
from datetime import datetime, time
from odoo import models, fields, api



class membersline(models.Model):
    _name = 'members.line'
    _description = 'members_line'

    name_id = fields.Many2one('hr.employee',string='اسم العضو', states={'confirm': [('readonly', False)]})
    # no_employee = fields.Integer(string="الرقم الوظيفي")
    # position = fields.Selection([('h1', 'عضو'), ('h2', 'مقرر'), ('h3', 'رئيس')], string="المنصب")
    member_id = fields.Many2one('masad.association', string='members line')
    # mangement = fields.Char(string="الادارة")
    coment = fields.Text(string="تعليق العضو")
    agree = fields.Char(string="الحالة",compute='_onchange_agree')
    solution = fields.Boolean(string='الموافقه')
    user_id = fields.Many2one('res.users', string='user_id', related='name_id.user_id',default=lambda self: self.env.user.id)



    @api.onchange('solution')
    def _onchange_agree(self):
        for record in self:
            if record.solution == True:
                record.agree = 'موافق'
            else:
                record.agree = 'غير موافق'


# #دالة البحث
    @api.onchange('user_id')
    def _onchange_employee(self):
        for rec in self:
           if rec.user_id:
               print("ddddd",rec.user_id)
               employee_id = self.env['hr.employee'].search([('user_id', '=', rec.user_id.id)], limit=1)
               print("reeeeeeeeeee",employee_id.id)
               rec.name_id=employee_id.id
