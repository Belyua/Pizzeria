from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .basket import Basket
from home.models import Product


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        product_qty = product_id = int(request.POST.get('productqty'))
        basket.add(product=product, qty=product_qty)
        response = JsonResponse({'qty': product_qty})
        return response
