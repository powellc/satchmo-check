"""
Handle a check-then-delivery payment.
"""
from django.utils.translation import ugettext as _
from payment.modules.base import BasePaymentProcessor, ProcessorResult

class PaymentProcessor(BasePaymentProcessor):
    """Check Payment Processor"""

    def __init__(self, settings):
        super(PaymentProcessor, self).__init__('check', settings)

    def capture_payment(self, testing=False, order=None, amount=None):
        """
        Check is always successful.
        """
        if not order:
            order = self.order

        # Check always results in a full balance until the check arrives.
        payment = self.record_payment(order=order, amount=0,
            transaction_id="CHECK", reason_code='0')

        return ProcessorResult(self.key, True, _('Success'), payment)

