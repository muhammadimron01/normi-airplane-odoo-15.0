from odoo import api, fields, models


class Flight(models.Model):
    _name = 'normiairplane.flight'
    _description = 'Flight Item'

    code = fields.Char(string='Flight Code')
    source = fields.Selection(string='Source', 
                              selection=[
                                ('jakarta', 'Jakarta'),
                                ('bandung', 'Bandung'),
                                ('semarang', 'Semarang'),
                                ('yogyakarta', 'Yogyakarta'),
                                ('surabaya', 'Surabaya'),
                                ('bali', 'Bali'),
                                ('lombok', 'Lombok'),
                                ('batam', 'Batam'),
                                ('medan', 'Medan'),
                                ('padang', 'Padang'),
                                ('pekanbaru', 'Pekanbaru'),
                                ('palembang', 'Palembang'),
                                ('tanjung_pinang', 'Tanjung Pinang'),
                                ('lampung', 'Lampung'),
                              ])
    destination = fields.Selection(string='Destination', 
                                   selection=[
                                        ('jakarta', 'Jakarta'),
                                        ('bandung', 'Bandung'),
                                        ('semarang', 'Semarang'),
                                        ('yogyakarta', 'Yogyakarta'),
                                        ('surabaya', 'Surabaya'),
                                        ('bali', 'Bali'),
                                        ('lombok', 'Lombok'),
                                        ('batam', 'Batam'),
                                        ('medan', 'Medan'),
                                        ('padang', 'Padang'),
                                        ('pekanbaru', 'Pekanbaru'),
                                        ('palembang', 'Palembang'),
                                        ('tanjung_pinang', 'Tanjung Pinang'),
                                        ('lampung', 'Lampung'),
                                   ])
    take_of = fields.Datetime(string='Take Of Date')
    seat = fields.Integer(string='Seats')
