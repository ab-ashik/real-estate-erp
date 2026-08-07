# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ReProject(models.Model):
    _name = 're.project'
    _description = 'Real Estate Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    code = fields.Char(required=True, tracking=True)
    active = fields.Boolean(default=True)
    status = fields.Selection(
        [
            ('upcoming', 'Upcoming'),
            ('running', 'Running'),
            ('completed', 'Completed'),
            ('archived', 'Archived'),
        ],
        default='upcoming',
        required=True,
        tracking=True,
    )
    location = fields.Char()
    progress_percent = fields.Float(string='Construction Progress %')
    flat_ids = fields.One2many('re.flat', 'project_id', string='Flats')
    flat_count = fields.Integer(compute='_compute_flat_count')

    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Project code must be unique.'),
    ]

    @api.depends('flat_ids')
    def _compute_flat_count(self):
        for rec in self:
            rec.flat_count = len(rec.flat_ids)
