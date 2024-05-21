from django.http import JsonResponse
from django.shortcuts import render
from .models import Product


# Create your views here.


def index(request):

    products = Product.objects.order_by('id').reverse()

    print(products)
    # return data in html page
    return render(request, 'index.html', {'products': products})  

