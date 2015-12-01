# This file is part of the account_invoice_total module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class AccountInvoiceTotalTestCase(ModuleTestCase):
    'Test Account Invoice Total module'
    module = 'account_invoice_total'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountInvoiceTotalTestCase))
    return suite

