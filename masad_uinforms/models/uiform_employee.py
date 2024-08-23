""""
This file uinform employee masad
Author: MASAD - HQ
"""

from odoo import models, fields, api, _
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare

class Uinformemployeline(models.Model):
    _name = 'uinform.employee.line'
    _description = 'This model is used uinform employee line'

    employee_line_id = fields.Many2one('hr.employee', string='Employe Name')
    gender = fields.Selection(related='employee_line_id.gender', string="Gender", store=True, readonly=True)
    name = fields.Char(string="Employee NO", related='employee_line_id.no_employee', store=True, readonly=False,racking=True)
    type_items_id = fields.Many2one('type.items', string='Items')
    categ_id = fields.Many2one('catgegory.employee',string='Category')
    color_items_id = fields.Char(string='Color Details')
    size_items_id = fields.Char(string='Size Details')
    color_id = fields.Many2one('color.items', string='Color')
    size_id = fields.Many2one('size.items', string='Size')
    date= fields.Date('Date')
    qty = fields.Integer(string='QTY')
    uinform_id = fields.Many2one('uinform.employee', string='uinform line')
    product_code = fields.Char(compute='_compute_amount',string="product code", store=True)

    @api.depends('type_items_id')
    def _compute_amount(self):
        for line in self:
            if line.type_items_id.code:
                line.product_code = str(line.type_items_id.name.name) +str('-') + str(line.type_items_id.code)
            else:
                line.product_code = line.type_items_id.name.name

#----------------------------------------
    @api.model
    def create(self, vals):
        get_property = self.env['uinform.employee'].search([('id', '=', vals['uinform_id'])])
        print("ppppppppppppppppppp",get_property)
        for rec in get_property:
               rec.uiform_line_ids.employee_line_id = get_property.employee_id.id
               rec.uiform_line_ids.categ_id = get_property.categ_id.id
               rec.uiform_line_ids.date = get_property.date
               rec.uiform_line_ids.name = get_property.name
        return super(Uinformemployeline, self).create(vals)
    

# class that defines uinform of employee
class Uinformemploye(models.Model):
    _name = 'uinform.employee'
    _description = 'This model is used uinform employee'

    name = fields.Char(string="Employee NO", related='employee_id.no_employee', store=True, readonly=False, tracking=True)
    gender = fields.Selection(related='employee_id.gender', string="Gender", store=True, readonly=True)
    employee_id = fields.Many2one('hr.employee', string='Employe Name')
    categ_id = fields.Many2one('catgegory.employee', string='Category')
    description = fields.Text('Description')
    date= fields.Date('Date')
    uiform_line_ids= fields.One2many('uinform.employee.line', 'uinform_id', string='uinform all')


class Uinformemployeline_technical(models.Model):
    _name = 'uinform.employee.line.technical'
    _description = 'This model is used uinform employee line'

    employee_line_id = fields.Many2one('hr.employee', string='Employe Name')
    gender = fields.Selection(related='employee_line_id.gender', string="Gender", store=True, readonly=True)
    name = fields.Char(string="Employee NO", related='employee_line_id.no_employee', store=True, readonly=False,racking=True)
    type_items_id = fields.Many2one('type.items', string='Items')
    categ_id = fields.Many2one('catgegory.employee',string='Category')
    color_items_id = fields.Char(string='Color Details')
    size_items_id = fields.Char(string='Size Details')
    color_id = fields.Many2one('color.items', string='Color')
    size_id = fields.Many2one('size.items', string='Size')
    date= fields.Date('Date')
    qty = fields.Integer(string='QTY')

    product_code = fields.Char(compute='_compute_amount',string="product code", store=True)
    #uinform_id = fields.Many2one('uinform.employee', string='uinform line')

    @api.depends('type_items_id')
    def _compute_amount(self):
        for line in self:
            if line.type_items_id.code:
                line.product_code = str(line.type_items_id.name.name) +str('-') + str(line.type_items_id.code)
            else:
                line.product_code = line.type_items_id.name.name


class Employee(models.Model):
    _inherit = 'hr.employee'

    no_employee= fields.Char('NO Employee')









