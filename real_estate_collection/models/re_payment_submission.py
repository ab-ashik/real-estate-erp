# -*- coding: utf-8 -*-
from odoo import fields, models


class RePaymentSubmission(models.Model):
    _name = 're.payment.submission'
    _description = 'Payment Submission'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(default='New', copy=False)
    partner_id = fields.Many2one('res.partner', required=True, tracking=True)
    allotment_id = fields.Many2one('re.allotment', required=True)
    target_id = fields.Many2one('re.payment.target', required=True)
    amount_bdt = fields.Monetary(currency_field='currency_id', required=True)
    payment_date = fields.Date(required=True, default=fields.Date.context_today)
    method = fields.Selection(
        [
            ('bank_deposit', 'Bank Deposit'),
            ('transfer', 'Bank Transfer'),
            ('cheque', 'Cheque'),
            ('pay_order', 'Pay Order'),
            ('cash', 'Cash'),
            ('bkash', 'bKash'),
            ('nagad', 'Nagad'),
        ],
        required=True,
    )
    paid_from = fields.Char(string='Paid / Deposited From', required=True)
    paid_to = fields.Char(string='Paid To (Company)', required=True)
    reference = fields.Char(string='Reference / Slip No.', required=True)
    evidence = fields.Binary(string='Evidence', attachment=True, required=True)
    evidence_filename = fields.Char()
    remarks = fields.Text()
    reject_reason = fields.Text()
    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id,
    )
    state = fields.Selection(
        [
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ],
        default='pending',
        tracking=True,
    )
