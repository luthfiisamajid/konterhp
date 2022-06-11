from odoo import api, fields, models

class penjualan(models.Model):
    _name = 'konterhp.penjualan'
    _description = 'Detail Penjualan'


    name = fields.Many2one(comodel_name='konterhp.pegawai', string='Kasir')
    
    kode_penjualan = fields.Char(string='Kode Penjualan')
    tanggal_penjualan = fields.Date(string='Tanggal Penjualan',default=fields.Date.today)
    dtlpnjln = fields.One2many(comodel_name='konterhp.detail_penjualan',
                                     inverse_name='detpenjualan_ids',
                                     string='Detail Penjualan')
    total_harga = fields.Integer(compute='_compute_total_harga', string='total_harga')
    
    @api.model
    def _compute_total_harga(self):
        for record in self:
            total=sum(self.env['konterhp.detail_penjualan'].search([('detpenjualan_ids','=',record.id)]).mapped('jumlah_harga'))
            record.total_harga=total
    
    
