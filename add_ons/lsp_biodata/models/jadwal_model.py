# -*- coding: utf-8 -*-
from odoo import fields, models

class Jadwal(models.Model):
    _name = 'lsp.jadwal'
    _description = 'Dokumen Description'

    period = fields.Char(string='Period', required=True)
    upload_file = fields.Binary(string="Upload File")
    file_name = fields.Char(string="File Name")
    result = fields.Char(string='Result', required=True)
    state = fields.Selection(string="Status", selection=[('draft', 'Draft'), ('confirm', 'Confirm'),
                                                         ('validate', 'Validated'), ('refuse', 'Refuse'),
                                                         ('approved', 'Approved'), ], default="draft", track_visibility='onchange', )