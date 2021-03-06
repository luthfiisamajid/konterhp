from odoo import api, fields, models

class barang(models.Model):
    _name = 'konterhp.barang'
    _description = 'New Description'

    name = fields.Char(string='Nama Barang')
    harga = fields.Integer(string='Harga Barang')
    stok = fields.Integer(string='Stok')
    harga_jual = fields.Integer(string='Harga Jual')
    pemasok = fields.Many2one(comodel_name='konterhp.supplier', string='Pemasok')
    jenis_id = fields.Many2one(comodel_name='konterhp.jenis', string='Jenisnya')
    laba = fields.Char(compute='_compute_laba', string='laba')

    @api.depends('harga','harga_jual')
    def _compute_laba(self):
        for record in self:
            record.laba = record.harga_jual - record.harga

    diskon = fields.Char(compute='_compute_diskon', string='diskon')
    
    @api.depends('harga_jual')
    def _compute_diskon(self):
        for record in self:
            if(record.harga_jual)<2200000:
                record.diskon = record.harga_jual *0.95
            else:
                record.diskon = record.harga_jual * 0.9


    comment_stok = fields.Char(compute='_compute_comment_stok', string='comment_stok')
    
    @api.depends('stok')
    def _compute_comment_stok(self):
        for record in self:
            if record.stok < 30:
                record.comment_stok = 'stok menipis'
            else:
                record.comment_stok = 'stok aman'        

    order_id = fields.Many2one(comodel_name='konterhp.detail_penjualan', string='Order')