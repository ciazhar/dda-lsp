# -*- coding: utf-8 -*-
from odoo import fields, models

class Biodata(models.Model):
  _inherit = 'res.partner'
  _name = 'biodata.s'
  _description = 'Biodata Description'

  name = fields.Char(string='Name', required=True)
  nik = fields.Char(string='Nik', required=True)
  tempat_lahir = fields.Char(string='Tempat Lahir')
  tanggal_lahir = fields.Char(string='Tanggal Lahir')
  jenis_kelamin = fields.Selection([('male', 'Male'),('female', 'Female')])
  alamat = fields.Char(string='Alamat')
  phone = fields.Char(string='Phone Number')
  email = fields.Char(string='Email', required=True)
  pendidikan_terakhir = fields.Char(string='Pendidikan Terakhir')
  skema_sertifikasi = fields.Char(string='Skema Sertifikasi')
  user_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user)
  accessor = fields.Boolean("isAccessor", default=False)

  _sql_constraints = [
    ('nim_unique',
      'UNIQUE(nim)',
      "The NIM must be unique"),
    ('nik_unique',
      'UNIQUE(nik)',
      "The NIK must be unique"),
    ('email_unique',
      'UNIQUE(email)',
      "The EMAIL must be unique"),
  ]