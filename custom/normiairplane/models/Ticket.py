from odoo import api, fields, models


class Ticket(models.Model):
    _name = 'normiairplane.ticket'
    _description = 'Ticket'

    name = fields.Char(string='Ticket Code')
    passenger_id = fields.Many2one(comodel_name='normiairplane.passenger', 
                                    string='Passengers')
    flight_id = fields.Many2one(comodel_name='normiairplane.flight', 
                                 string='Flights')
    gender = fields.Char(compute='_compute_gender', string='gender')
    passport = fields.Char(string='Passport Number')
    nationality = fields.Char(string='Nationality')
    price = fields.Integer(compute='_compute_price', string='Price')
    
    @api.depends('passenger_id')
    def _compute_gender(self):
        for rec in self:
            passenger = self.env['normiairplane.passenger'].search([])
            rec.gender = passenger.gender
            rec.passport = passenger.passport
            rec.nationality = passenger.nationality
    
    @api.depends('flight_id')
    def _compute_price(self):
        for rec in self:
            flight = self.env['normiairplane.flight'].search([])
            rec.price = flight.price