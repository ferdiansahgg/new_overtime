# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
from datetime import datetime, timedelta


class new_overtime(models.Model):
    _name = "hr.overtime"
    _inherit = "hr.overtime"

    @api.onchange("date_from")
    def action_hari(self):
        if self.date_from != 0:
            self.date_to = self.date_from + timedelta(days=30)
            a = self.date_to
            a = int(a.strftime("%d"))
            self.number_of_hours_temp = a * 24

    #     date1 = self.date_from
    #     date2 = self.date_to
    #     obj_date1 = datetime.strptime(str(date1, "%d/%b/%Y %H:%M:%S"))
    #     obj_date2 = datetime.strptime(str(date2, "%d/%b/%Y %H:%M:%S"))
    #     duration = obj_date1 - obj_date2
    #     seconds = duration.total_seconds()
    #     d = divmod(seconds, 86400)
    #     self.number_of_hours_temp = = divmod(d[1], 3600)

    # self.number_of_hours_temp = 30*self.date_to + 24*self.date_from

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

