"""Simple wrapper for standard checkout as implemented in payment.views"""

from django.views.decorators.cache import never_cache
from livesettings import config_get_group
from payment.views import confirm, payship
    
check = config_get_group('PAYMENT_CHECK')
    
def pay_ship_info(request):
    return payship.simple_pay_ship_info(request, config_get_group('PAYMENT_CHECK'), 'shop/checkout/check/pay_ship.html')
pay_ship_info = never_cache(pay_ship_info)
    
def confirm_info(request):
    return confirm.credit_confirm_info(request, check, template='shop/checkout/check/confirm.html')
confirm_info = never_cache(confirm_info)

