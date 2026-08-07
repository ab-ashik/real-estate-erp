# -*- coding: utf-8 -*-
from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    re_force_password_change = fields.Boolean(
        string='Force Password Change',
        help='User must change password on next login.',
    )
