# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
  _inherit = 'res.bio'

  todo_ids = fields.Many2many('biodata.s', string='Bidata Creator')