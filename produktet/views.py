from django.shortcuts import render,get_object_or_404
from .models import Product


def produktet(request):
    full_produktet=Product.objects.order_by()
    data={
        'full_produktet':full_produktet,

    }
    return render(request, 'produktet/produktet.html',data)


def produktet_detail(request, id):
    produkt = get_object_or_404(Product,pk=id)
    data={
        'produkt':produkt,
    }
    return render(request, 'produktet/produktet_detail.html',data) 
