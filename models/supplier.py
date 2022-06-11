from odoo import api, fields, models

class supplier(models.Model):
    _name = 'konterhp.supplier'
    _description = 'Pemasok Barang Konterhp'

    name = fields.Char(string='Nama Perusahaan')
    cp = fields.Char(string='Contact_Person')
    no_tlp = fields.Char(string='No_tlp')
    alamat = fields.Char(string='Alamat')
    barang_ids = fields.One2many(comodel_name='konterhp.barang',inverse_name='pemasok',string='Barangnya')