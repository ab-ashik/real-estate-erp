# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    re_partner_type = fields.Selection(
        [
            ('flat_buyer', 'Flat Buyer'),
            ('project_dealer', 'Project Dealer'),
        ],
        string='Role in Project',
        help='How this person relates to your projects: end flat buyer or dealer.',
    )
    re_status = fields.Selection(
        [
            ('awaiting_booking_deposit', 'Awaiting Booking Deposit'),
            ('active_allottee', 'Active Allottee'),
        ],
        default='awaiting_booking_deposit',
        string='Allottee Status',
        help='Awaiting Booking Deposit = registered but first approved booking/initial '
             'payment not done yet. Active Allottee = has approved deposit on an allotted flat.',
    )
    nid = fields.Char(
        string='National ID (NID)',
        help='Bangladesh National ID of the flat buyer / dealer.',
    )
