# -*- coding: utf-8 -*-
from odoo import fields, models


class RePaymentTarget(models.Model):
    _name = 're.payment.target'
    _description = 'Payment Target'
    _order = 'due_date, id'

    name = fields.Char(required=True)
    allotment_id = fields.Many2one('re.allotment', required=True, ondelete='cascade', index=True)
    amount_bdt = fields.Monetary(currency_field='currency_id', required=True)
    paid_bdt = fields.Monetary(currency_field='currency_id', default=0.0)
    due_date = fields.Date(required=True)
    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id,
    )
    state = fields.Selection(
        [
            ('open', 'Open'),
            ('partial', 'Partial'),
            ('paid', 'Paid'),
            ('overdue', 'Overdue'),
        ],
        default='open',
    )
