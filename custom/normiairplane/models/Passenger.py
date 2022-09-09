from odoo import api, fields, models


class Passenger(models.Model):
    _name = 'normiairplane.passenger'
    _description = 'Passenger'

    name = fields.Char(string='Passenger Name')
    nationality = fields.Selection([
        ('indonesia', 'Indonesia'),
        ('malaysia', 'Malaysia'),
        ('singapore', 'Singapore'),
    ], string='Nationality')
    gender = fields.Selection(selection=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    passport = fields.Char(string='Passport Number')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    
    
    
