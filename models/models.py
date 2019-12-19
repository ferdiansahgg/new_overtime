# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
from datetime import datetime, timedelta


class new_overtime(models.Model):
    _name = "hr.overtime"
    _inherit = "hr.overtime"

    @api.onchange("date_to")
    def action_hari(self):
        if self.date_to:
            DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
            from_dt = datetime.strptime(str(self.date_from), DATETIME_FORMAT)
            to_dt = datetime.strptime(str(self.date_to), DATETIME_FORMAT)
            timedelta = to_dt - from_dt
            diff_day = float(timedelta.days) * 24.0
            self.number_of_hours_temp = diff_day

    @api.onchange("department_id")
    def action_generate(self):
        obj_emp = self.env["hr.employee"].search(
            [("active", "=", True), ("department_id", "=", self.department_id.id)]
        )
        line_data = []
        for record in self:
            record.update({"employee_ids": False})
            for z in obj_emp:
                line_data = [(0, 0, {"employee_id": z.id,})]
                record.update({"employee_ids": line_data})


class vitcustom_overtime(models.Model):
    _name = "hr.employee"
    _inherit = "hr.employee"
    work_location = fields.Many2one(
        comodel_name="account.analytic.tag", string="Work Location"
    )

