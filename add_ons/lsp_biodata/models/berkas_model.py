# -*- coding: utf-8 -*-
from odoo import fields, models

class Berkas(models.Model):
    _name = 'lsp.berkas'
    _description = 'Berkas Description'

    name = fields.Char(string='Name', required=True)
    upload_file = fields.Binary(string="Upload File")
    file_name = fields.Char(string="File Name")
    state = fields.Selection(string="Status", selection=[('draft', 'Draft'), ('confirm', 'Confirm'),
                                                     ('validate', 'Validated'), ('refuse', 'Refuse'),
                                                     ('approved', 'Approved'), ], default="draft", track_visibility='onchange', )