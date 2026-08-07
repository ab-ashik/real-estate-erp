# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class RealEstatePortal(http.Controller):
    """Scaffold — portal routes in later sprint."""

    @http.route('/my/re', type='http', auth='user', website=True)
    def re_home(self, **kwargs):
        return request.render('real_estate_portal.portal_my_re_home', {})
