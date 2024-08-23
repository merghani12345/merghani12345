""""
This file represents configuration models for the module
Author: MASAD - HQ
"""
from odoo import models, fields


class Catgegoryemployee(models.Model):
    _name = 'catgegory.employee'
    _description = 'types Catgegory.'

    name = fields.Char('Catgegory Name')
    code = fields.Integer('Sequence')
########################################################################################################################
class Typesitems(models.Model):
    _name = 'type.items'
    _description = 'types items.'

    name = fields.Many2one('product.product',string='Items')
    designing_ar = fields.Text(string="مواصفات النوع")
    designing_en = fields.Text(string="Designing Descriptions English")

    specification_ar = fields.Text(string="مواصفات القماش او الخام")

    specification_en = fields.Text(string="FABRIC & MATERIAL SPECIFICATION")

    type_items = fields.Selection(string='Type',selection=[
        ('suit_vip', 'SUIT VIP'), ('suit_regulars', 'SUIT Regulars'),
        ('suit_shirt', 'SUIT Shirt'),('belt', 'Belt'),
        ('casual_jacket ', 'Casual Jacket'),('drivers_safari', 'Drivers Safari'),
        ('trouser ', 'Trouser'), ('shirt_long_sleeves ', 'Shirt long sleeves'),
        ('shirt_long_sleeves_ladies ', 'Shirt long sleeves ladies'), ('skirt', 'Skirt'),
        ('scarf ', 'Scarf'), ('cargo_trouser', 'Cargo trouser'),
        ('labor_trouser ', 'Labor Trouser'), ('t_Shirt', 'T-Shirt'),
        ('shoes ', 'Shoes'), ('belt', 'Belt'),
        ('socks ', 'Socks'), ('tie', 'Tie'),
    ], default='suit_vip')
    code = fields.Char('Code SPECIFICATION')
    #product_qty = fields.Integer(string='product QTY',compute='_compute_qty')

   # @api.depends('name')
    #def _compute_qty(self):

        #product_id = self.env['res.currency'].browse(currency_id)
       # obj_line = self.env['uinform.employee.line'].browse(type_items_id)

        #journal = self.env['account.journal'].browse(context.get('journal_id'))

       # print("qqqqqqqqqobj_lineobj_lineobj_lineobj_lineqqqqqqq", obj_line)

      #  for line in self:

         #   product = self.env['uinform.employee.line'].search([('type_items_id', '=', line.name.id)])
          #  print("ppppppppppppddddd",product)
           # qty = 0
            #obj_line = self.env['uinform.employee.line'].browse(line.name.id)
          #  print("testtttttttssssssssssssssssssstttt",obj_line)

            #for record in  product:
             #   print("recccccccccc",record)
               # print("zzzzzzzzzzzzzzzzzzzzzzzzzzz",line.name.name,"snaaaaaaaaaaa",record.type_items_id.name.name)
               # if line.name.id==record.type_items_id.name:
            #        qty+=record.qty
                  #  print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",qty)

           # print("qqqqqqqqqqxxxxxxxxxxxxxxxxxxxxqqqqqq", qty)

            #line.product_qty=qty
                  #  line.product_code = str(line.type_items_id.name.name) + str('-') + str(line.type_items_id.code)


########################################################################################################################
# inherit res.users to link salesperson to estate property
class Coloritems(models.Model):
    _name = 'color.items'
    _description = 'color items'

    name = fields.Char('Color',)
    color = fields.Integer('Color', default=0)
    code = fields.Char('Code')

class Sizeitems(models.Model):
    _name = 'size.items'
    _description = 'color items'

    name = fields.Char('Size', required=True)
    code = fields.Char('Code')



class memberuniform(models.Model):
    _name = 'member.unifrom'
    _description = 'attachment line'
    _rec_name = 'employee_id'
    name = fields.Char(string="Employee NO", related='employee_id.no_employee', store=True, readonly=False)
    employee_id = fields.Many2one('hr.employee', string='Employe Name')

    department_id = fields.Many2one('hr.department', related='employee_id.department_id', string='الادارة', store=True)

    job_member = fields.Char(string="الصفة")
   # member_id = fields.Many2one('uniform.attachment', string='الاعضاء')







#المحضر
class uniformattachmentline(models.Model):
    _name = 'uniform.attachment.line'
    _description = 'attachment line'


    name = fields.Char(string="اسم المرفق")

    batchfile = fields.Binary("المرفق")
    attachment_id = fields.Many2one('uniform.attachment', string='attachment')
class member_task(models.Model):
    _name = 'member.task'
    _description = 'member task'

    name = fields.Char(string="التكاليف")
    member_task = fields.Char(string="المكلف")
    period_task = fields.Char(string="الفترة")
    mark_task = fields.Char(string="ملاحظات")
    task_id = fields.Many2one('uniform.attachment',string='التكاليف')



# class that defines uinform of employee
class uniformattachment(models.Model):
    _name = 'uniform.attachment'
    _description = 'This model is used uinform employee'

    name = fields.Char(string="رقم الاجتماع")
    location = fields.Char(string="مكان الاجتماع")
    description = fields.Text('الاجندة')
    description2 = fields.Text('التوصيات')
    date = fields.Date('Date')
    start_date = fields.Date('Start Date')

    attachment_line_ids = fields.One2many('uniform.attachment.line', 'attachment_id', string='attachment')
    empo_attachment_line_ids = fields.One2many('member.unifrom.line', 'member_id', string='الحضور')

    empo_attachment_line_ids2 = fields.One2many('member.unifrom.line', 'member_id2', string='الاعتذار')


    task_ids = fields.One2many('member.task', 'task_id', string='التكاليف')



class memberuniformline(models.Model):
    _name = 'member.unifrom.line'
    _description = 'member line'
    _rec_name = 'employee_id'
   # name = fields.Char(string="Employee NO", related='employee_id.no_employee', store=True, readonly=False, tracking=True)
    employee_id = fields.Many2one('member.unifrom', string='Employe Name')

    department_id = fields.Many2one('hr.department', related='employee_id.department_id', string='الادارة', store=True)

    job_member = fields.Char(string="الصفة",related='employee_id.job_member')
    member_id = fields.Many2one('uniform.attachment', string='الحضور')

    member_id2 = fields.Many2one('uniform.attachment', string='الاعتذار')





