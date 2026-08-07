# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ReFlat(models.Model):
    _name = 're.flat'
    _description = 'Real Estate Flat'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(compute='_compute_name', store=True)
    code = fields.Char(required=True, tracking=True)
    project_id = fields.Many2one('re.project', required=True, ondelete='restrict', index=True)
    floor = fields.Char()
    flat_type = fields.Char(string='Type')
    size_sft = fields.Float(string='Size (sft)')
    price_bdt = fields.Monetary(currency_field='currency_id', string='Price (BDT)')
    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id,
    )
    status = fields.Selection(
        [
            ('available', 'Available'),
            ('hold', 'Hold'),
            ('booked', 'Booked'),
            ('sold', 'Sold'),
        ],
        default='available',
        required=True,
        tracking=True,
    )

    _sql_constraints = [
        ('project_code_uniq', 'unique(project_id, code)', 'Flat code must be unique per project.'),
    ]

    @api.depends('project_id.code', 'code')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.project_id.code or ''}/{rec.code or ''}"
