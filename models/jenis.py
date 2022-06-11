from odoo import api, fields, models

class jenis(models.Model):
    _name = 'konterhp.jenis'
    _description = 'New Description'

    name = fields.Char(string='Jenis Barang')
    deskripsi = fields.Char(string='Deskripsi')
    letak = fields.Char(string='Letak Barang')
    barang_ids = fields.One2many(comodel_name='konterhp.barang', inverse_name='jenis_id', string='Jenisnya')
    
