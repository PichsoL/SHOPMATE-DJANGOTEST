from django.shortcuts import render
from store.models import Product 

def home(request): #function called home that take in request 
    products = Product.objects.all().filter(is_available=True)#only bring the products that are available 
    context = {
        'products': products,  
    }
    return render(request, 'home.html', context)