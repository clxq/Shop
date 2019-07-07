from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                cart.clear()
                return render(request, "order/success.html", locals())
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', locals())


from alipay import AliPay
from django.conf import settings
import os
import time


def pay(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
    total_price = request.POST.get('price')
    ali_pay = AliPay(
        appid=settings.ALIPAY_APPID,
        app_notify_url=None,
        app_private_key_path=os.path.join(settings.BASE_DIR,
                                          'trade/keys/pri_2048.txt'),
        alipay_public_key_path=os.path.join(settings.BASE_DIR,
                                            'trade/keys/pub_2048.txt'),
        sign_type="RSA2",
        debug=True
    )
    order_string = ali_pay.api_alipay_trade_page_pay(
        subject="Shopping",
        out_trade_no=int(time.time()),
        total_amount=total_price,
        return_url='http://127.0.0.1:8000/order/success',
        notify_url=None
    )
    # 拼接参数
    url = settings.ALIPAY_URL + "?" + order_string
    return redirect(url)


def order_success(request):
    out_trade_no = request.GET.get("out_trade_no")
    trade_no = request.GET.get('trade_no')
    total_amount = request.GET.get('total_amount')
    seller_id = request.GET.get("seller_id")
    return render(request, "order/success.html", locals())