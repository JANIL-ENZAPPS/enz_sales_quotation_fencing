from odoo import fields,models

class SaleReportFormatDetails(models.Model):
    _name = 'sale.report.format.details'
    _rec_name = 'name'
    _description = 'Sale Report Format Details'

    name = fields.Char(default="Sale Report Format")
    terms_and_condition_id = fields.One2many('sale.report.format.terms.and.condition','format_id')
    note_id = fields.One2many('sale.report.format.note.details','format_id')
    payment_condition_id = fields.One2many('payment.conditions.details','format_id')
    client_scope_id = fields.One2many('client.scope.details','format_id')
    contractor_scope_id = fields.One2many('contractor.scope.details','format_id')
    activated = fields.Boolean(default=True)
    stamp_img = fields.Binary()
    account_name = fields.Char()
    bank_name = fields.Char()
    account_number = fields.Char()
    iban_number = fields.Char()
    arabic_account_name = fields.Char()
    arabic_bank_name = fields.Char()

class SaleReportFormatTermsAndCondition(models.Model):
    _name = 'sale.report.format.terms.and.condition'
    _rec_name = 'name'
    _description = 'Sale Report Format Terms And Condition'

    format_id = fields.Many2one('sale.report.format.details')
    name = fields.Char()


class SaleReportFormatNoteDetails(models.Model):
    _name = 'sale.report.format.note.details'
    _rec_name = 'name'
    _description = 'Sale Report Format Note Details'


    format_id = fields.Many2one('sale.report.format.details')
    name = fields.Char()


class PaymentConditionsDetails(models.Model):
    _name = 'payment.conditions.details'
    _rec_name = 'name'
    _description = 'Payment Conditions Details'


    format_id = fields.Many2one('sale.report.format.details')
    name = fields.Char()


class ClientScopeDetails(models.Model):
    _name = 'client.scope.details'
    _rec_name = 'name'
    _description = 'Client Scope Details'

    format_id = fields.Many2one('sale.report.format.details')
    name = fields.Char()


class ContractorScopeDetails(models.Model):
    _name = 'contractor.scope.details'
    _rec_name = 'name'
    _description = 'Contractor Scope Details'

    format_id = fields.Many2one('sale.report.format.details')
    name = fields.Char()