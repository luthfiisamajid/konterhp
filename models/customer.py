from odoo import api, fields, models

class customer(models.Model):
    _name = 'konterhp.customer'
    _description = 'Detail Customer'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    no_tlp = fields.Char(string='No Telepon')
    
    
