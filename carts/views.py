from django.shortcuts import get_object_or_404, render, redirect
from store.models import Product
from . models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from django.http import HttpResponse
def _cart_id(request): 
    cart = request.session.session_key 
    if not cart: 
        cart = request.session.create()
    return cart 

def add_cart(request, product_id): 
    product = Product.objects.get(id = product_id) # get the product 
    try: 
        cart = Cart.objects.get(cart_id = _cart_id(request))# get the cart using the cart_id present in the session 
    except Cart.DoesNotExist: 
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save() # to save the file 
    #PUT PRODUCT INSIDE THE CART -> SO THE PRODUCT BECOMES CART ITEMS 
    try: 
        cart_item = CartItem.objects.get(product = product, cart = cart)
        cart_item.quantity += 1 #increment the cart item quantity by 1 
        cart_item.save() 
    except CartItem.DoesNotExist: 
        cart_item = CartItem.objects.create(
            product = product, 
            quantity = 1, 
            cart = cart, 
        )
        cart_item.save()
    return redirect('cart')

def remove_cart(request, product_id):# pass in the request and product_id
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id = product_id) #if the object is present, it will return the object, otherwise it return false 
    cart_item = CartItem.objects.get(product=product, cart = cart)#bring us the cart item 
    if cart_item.quantity > 1: 
        cart_item.quantity -= 1  #decrement the product quantity by 1 
        cart_item.save() 
    else: 
        cart_item.delete()
    return redirect('cart')#redirect to the cart page 

def remove_cart_item(request, product_id): 
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id = product_id)
    cart_item = CartItem.objects.get(product = product, cart = cart)
    cart_item.delete() #delete the item if the remove button is clicked 
    return redirect('cart')


def cart(request, total = 0, quantity = 0, cart_items = None): 
    try: 
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart = cart, is_active = True)
        for cart_item in cart_items: #loop through each cart item 
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity 
        tax = (2*total)/100 #apply 2 percent of tax on the total amount 
        grand_total = total + tax 
    except ObjectDoesNotExist: 
        pass #just ignore 
        
    context = {
        'total': total, 
        'quantity': quantity, 
        'cart_items': cart_items, 
        'tax': tax, 
        'grand_total': grand_total
    }
    return render(request, 'store/cart.html', context)