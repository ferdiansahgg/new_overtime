# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
from datetime import datetime, timedelta


class new_overtime(models.Model):
    _name = "hr.overtime"
    _inherit = "hr.overtime"

    @api.onchange("date_from")
    def _calc_date(self):
        if self.date_from != 0:
            self.date_to = self.date_form + timedelta(days=30)

    @api.multi
    def action_generate(self):
        obj_emp = self.env["hr.employee"].search(
            [("active", "=", True), ("department_id", "=", self.department_id.id)]
        )
        line_data = []
        for record in self:
            for z in obj_emp:
                line_data = [(0, 0, {"employee_id": z.id,})]
                record.write({"employee_ids": line_data})


class vitcustom_overtime(models.Model):
    _name = "hr.employee"
    _inherit = "hr.employee"
    work_location = fields.Many2one(
        comodel_name="account.analytic.tag", string="Work Location"
    )

