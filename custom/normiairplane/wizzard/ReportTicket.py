from odoo import api, fields, models

class ReportTicket(models.TransientModel):
    _name = 'normiairplane.reportticket'
    _description = 'New Description'

    from_date = fields.Date(string='From')
    to_date = fields.Date(string='To')

    def action_report_ticket(self):
        pass
