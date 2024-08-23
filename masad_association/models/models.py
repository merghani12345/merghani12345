#-*- coding: utf-8 -*-
import selectors
from odoo import api, fields, models, tools, SUPERUSER_ID,exceptions, _
from datetime import datetime, time
from odoo import models, fields, api


class masad_association(models.Model):
    _name = 'masad.association'
    _description = 'masad_association.masad_association'


    state = fields.Selection([  ('draft', 'مسودة'),('to approve', 'قيد الراجعة'), ('confirm', 'الموافقة'),  ('done', 'اكتمل'), ('cancel', 'الغاء الطلب')],
    string='حالة الطلب', readonly=True,  default='draft',help="حالة الطلب")
    individual = fields.Selection([('a1', 'موظف'), ('b2', 'نظامي')], default='a1' ,string='تصنيف الفرد')
    classification = fields.Selection([('cf1', 'افراد'), ('cf2', 'مؤسسات')],default='cf1',string='تصنيف الطلب')
    name =  fields.Char(string='الاسم',required=True,help="ادخل الاسم الرباعي")
    ref = fields.Char(string='رقم الطلب' ,readonly=True,help="رقم الطلب")
    job_des = fields.Char(string="الوظيفة",help="ادخل الوظيفة")
    job_stat = fields.Selection([('js1', 'بالخدمة'), ('js2', 'معاش')],  string='الحالةالوظيفية')
    job_state = fields.Selection([('jse1', 'خاص'), ('jse2', 'جهة اعتبارية')], string='المستفيد')
    comment = fields.Char(string="تعليقات",help="ادخل تعليق على الطلب")
    monthly_salary = fields.Char(string="الراتب الشهري",help="المرتب الشهري")
    child_num = fields.Char(string="عدد الاطفال")
    id_card = fields.Selection([('id1','الرقم الوظيفي'),('id2','الرقم العسكري'),('id3','الرقم الوطني'),('id4','الرقم الضريبي'),('id5','رقم العقار')],string="بطاقة التعريف" ,help="ادخل رقم معرف الاثبات الشخصي")
    id_num = fields.Integer(string="رقم التعريف" )
    rank = fields.Selection(
        [('r1', 'جندي'), ('r2', 'وكيل عريف'), ('r3', 'عريف'), ('r4', 'رقيب'), ('r5', 'رقيب اول'), ('r6', 'مساعد'),
         ('r7', 'ملازم'), ('r8', 'ملازم اول'), ('r9', 'نقيب'),
         ('r10', 'رائد'), ('r11', 'مقدم'), ('r12', 'عقيد'), ('r13', 'عميد'), ('r14', 'لواء'), ('r15', 'فريق'),
         ('r16', 'فريق اول'), ('r17', 'مشير'), ('r18', 'رائد ركن'), ('r19', 'مقدم ركن'), ('r20', 'عقيد ركن'), ('r21', 'عميد ركن'), ('r22', 'لواء ركن'),
         ('r23', 'فريق ركن'),('r24', 'فريق اول ركن'), ('r25', 'مشير ركن')], string="الرتبة")
    company = fields.Char(string="الجهة التابع لها")
    case_details = fields.Char(string="تفاصيل الحالة")
    marital_status = fields.Selection([('ms1','متزوج'),('ms2','اعزب'),('ms3','مطلقة'),('ms4','ارملة')],string="الحالة الاجتماعية" )
    masad_type = fields.Char(string="نوع الالتحاق بالمنظومة")
    gender = fields.Selection([('gender1','ذكر'),('gender2','انثى')],string="النوع")
    age = fields.Char(string="العمر" )
    phone_num = fields.Char(string="رقم التلفون")
    address = fields.Char(string="العنوان")
    circle = fields.Char(string="الدائرة")
    boss = fields.Char(string="الرئيس المباشر")
    address_type = fields.Selection([('at1','ملك'),('at2','ايجار')],string="نوع السكن" )
    masad = fields.Selection([('msd1', 'نعم'), ('msd2', 'لا')], string="يتبع للمنظومة")
    company_type = fields.Selection([('ct1','حكومي'),('ct2','منظمات'),('ct3','خاصة'),('ct4','دار عبادة')],string="نوع المؤسسة" )
    description = fields.Text()
    receve_date = fields.Date(string='تاريخ استلام الطلب',help="هنا يدخل تاريخ استلام الطلب")
    request_date = fields.Date(string='تاريخ تقديم الطلب', required=True, readonly=True, index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, default=fields.Datetime.now, help="هنا يدخل تاريخ الطلب")
    support_tybe= fields.Selection([('s1', 'مباشر'), ('s2', 'غير مباشر')], string="نوع الدعم")
    categ_id = fields.Many2one('sp.line', string='تصنيف الدعم')
    support_details= fields.Text(string="تفاصيل الدعم" ,help="تفاصيل اضافية")
    price= fields.Integer(string= "المبلغ" ,digits='Product Price')
    currency_id = fields.Many2one('res.currency', string='العملة', required=True, default=lambda self: self.env.company.currency_id.id)
    member_ids = fields.One2many('members.line', 'member_id', string='member')
    test = fields.Selection([('p1','بيانات شخصية')],string="بيانات اضافية",help="اختار من داخل الصندوق بيانات اضافية")
    Doc = fields.Binary(string="المرفقات",help="اضف مستندات الطلب")
    total_price = fields.Char(string="المبلغ كتابة :",
                                    compute='_compute_number_to_words' ,readonly=True)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'مهم'),
        ('2', 'مهم جدا'),
        ('3', 'بالغ الاهمية')], string="الاهمية")

    def _compute_number_to_words(self):
        """Compute the amount to words in Sale Order"""
        for rec in self:
            rec.total_price = rec.currency_id.amount_to_text(rec.price)

    #دالة تمنع تكرار التصويت
    @api.onchange('member_ids')
    def _onchange_check_lines(self):
        if len(self.member_ids) > 1:
            raise exceptions.UserError("لا يمكنك التصويت مرة اخرى")


    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'] .next_by_code ('masad.association')
        return super(masad_association, self).create(vals)


    def button_approve(self):
        self.write({'state': 'to approve'})
        return {}
    def button_confirm(self):
        if not self.member_ids:
            raise exceptions.UserError(_("عفوا لايوجد تصويت"))
        else:
            self.write({'state': 'confirm'})
        return {}
    def button_done(self):
        self.write({'state': 'done'})
        return {}
    def button_cancel(self):
        self.write({'state': 'cancel'})
        return {}
    def button_to_draft(self):
        self.write({'state': 'draft'})
        return {}






