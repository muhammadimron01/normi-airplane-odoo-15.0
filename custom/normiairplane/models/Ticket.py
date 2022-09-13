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
    total = fields.Integer(string='Total')
    price = fields.Integer(compute='_compute_price', string='Price')
    
    @api.depends('passenger_id')
    def _compute_gender(self):
        for rec in self:
            passenger = self.env['normiairplane.passenger'].search([('id', '=', rec.passenger_id.id)])
            rec.gender = passenger.gender
            rec.passport = passenger.passport
            rec.nationality = passenger.nationality
    
    @api.depends('flight_id')
    def _compute_price(self):
        for rec in self:
            flight = self.env['normiairplane.flight'].search([('id', '=', rec.flight_id.id)])
            rec.price = flight.price * rec.total
    
    @api.model
    def create(self, vals):
        record = super(Ticket, self).create(vals)
        if record.flight_id:
            self.env['normiairplane.flight'].search([('id', '=', record.flight_id.id)]).write({'seat': record.flight_id.seat - record.total})
        return record
    
    @api.ondelete(at_uninstall=False)
    def _ondelete_flight_seat(self):
        if(self.flight_id):
            a = []
            for rec in self:
                a = self.env['normiairplane.flight'].search([('id', '=', rec.flight_id.id)])
            for ob in a:
                ob.seat += self.total