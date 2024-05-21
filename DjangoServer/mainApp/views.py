from django.http import JsonResponse
from .models import Product

# Create your views here.


def index(request):

    products = Product.objects.all()
    return JsonResponse({'products': list(products.values())})

