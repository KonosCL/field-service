# Copyright (C) 2019 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    require_vehicle_id = fields.Boolean(
        string='Require Vehicle',
        help="Stock Pickings with this enabled must have the vehicle "
             "set before they can reserve quantities. ",
        default=False)
