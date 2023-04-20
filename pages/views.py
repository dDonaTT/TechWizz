from django.shortcuts import render
from .models import Team
from produktet.models import Product    

def home(request):
    featured_products = Product.objects.order_by().filter(is_featured=True)
    full_produktet=Product.objects.order_by()
    data={
        'featured_products':featured_products,
        'full_produktet':full_produktet,

    }
    return render(request, 'pages/home.html',data)

def about(request):
    teams=Team.objects.all()
    data={
        'teams':teams,

    }
    return render(request, 'pages/about.html',data)
def produktet(request):
    return render(request, 'pages/produktet.html')
def contact(request):
    return render(request, 'pages/contact.html')
