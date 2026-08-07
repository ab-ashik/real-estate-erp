# -*- coding: utf-8 -*-
from odoo import fields, models


class ReAllotment(models.Model):
    _name = 're.allotment'
    _description = 'Real Estate Allotment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, copy=False, default='New')
    partner_id = fields.Many2one('res.partner', required=True, tracking=True)
    project_id = fields.Many2one('re.project', required=True, tracking=True)
    flat_id = fields.Many2one('re.flat', required=True, tracking=True)
    net_price_bdt = fields.Monetary(currency_field='currency_id')
    booking_money_bdt = fields.Monetary(currency_field='currency_id')
    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id,
    )
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled'),
        ],
        default='draft',
        tracking=True,
    )
