from odoo import api, fields, models

class detail_penjualan(models.Model):
    _name = 'konterhp.detail_penjualan'
    _description = 'New Description'

    name = fields.Many2one(comodel_name='konterhp.customer', string='Pembeli')
    
    jumlah_beli = fields.Integer(string='Jumlah Beli')
    jumlah_harga = fields.Integer(compute='_compute_jumlah_harga', string='Jumlah Harga')
    detailhp_id = fields.Many2one(comodel_name='konterhp.barang', string='Detail HP')
    hargahp = fields.Integer(compute='_compute_hargahp', string='Harga HP')
    
    
    @api.depends('detailhp_id')
    def _compute_hargahp(self):
        for record in self :
            record.hargahp = record.detailhp_id.harga_jual
    
    @api.depends('jumlah_beli','hargahp')
    def _compute_jumlah_harga(self):
        for record in self:
            record.jumlah_harga=record.jumlah_beli*record.hargahp
    
    detpenjualan_ids = fields.Many2one(comodel_name='konterhp.penjualan', string='Kasir')
