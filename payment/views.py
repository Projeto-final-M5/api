from django.shortcuts import render, redirect
import uuid
from django.contrib import messages
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings


def home(request):
    host = request.get_host()
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "30.00",
        "item_name": "book 1",
        "invoice": str(uuid.uuid4()),
        "currency_code": "USD",
        "notify_url": f'http://{host} { reverse("paypal-ipn")}',
        "return_url": f'http://{host}{ reverse("paypal_return")}',
        "cancel_return": f'http://{host}{ reverse("paypal_cancel")}',
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "home.html", context)


def paypal_return(request):
    messages.success(request, "deu certo")
    return redirect("home")


def paypal_cancel(request):
    messages.error(request, "não deu certo")
    return redirect("home")
