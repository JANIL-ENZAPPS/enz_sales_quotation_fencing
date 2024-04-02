from odoo import models,fields,api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    attention_id = fields.Many2one('res.partner')
    contact_id = fields.Many2one('res.partner')
    sale_format_id = fields.Many2one('sale.report.format.details')
    payment_term = fields.Char()
    rev = fields.Char(default="00")

    def date_formate_fix(self, date):
        if date:
            year, month, day = str(date).split('-')
            date = day + '/' + month + '/' + year
            return date

    def date_time_formate_fix(self, date):
        if date:
            date, time = str(date).split(' ')
            year, month, day = date.split('-')
            date = day + '/' + month + '/' + year
            return date

    def retrive_bank_account_details_branch(self):
        banks = self.env['branch.bank.account'].search([('branch_id','=',self.branch_id.id),('show_in_report','=',True)])
        return banks

    def retrive_formate_configuration(self):
        format = self.env['sale.report.format.details'].search([('activated','=',True)])
        if self.sale_format_id:
            format = self.sale_format_id
        else:
            format = format[0]
            self.sale_format_id = format[0].id
        if not format:
            return None
        else:
            return format