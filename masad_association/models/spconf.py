#-*- coding: utf-8 -*-

from odoo import models, fields, api


class spline(models.Model):
    _name = 'sp.line'
    _description = 'sp_line'

    name = fields.Char('اسم الدعم',required=True)
