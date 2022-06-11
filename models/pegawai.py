from odoo import api, fields, models

class pegawai(models.Model):
    _name = 'konterhp.pegawai'
    _description = 'List Pegawai'

    name = fields.Char(string='Name')
    jabatan = fields.Char(string='Jabatan')
    gaji = fields.Integer(string='Gaji')
    bonus = fields.Integer(string='Bonus')
    menikah = fields.Boolean(string='Menikah')
