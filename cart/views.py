from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Prodotti
from .cart import Cart
from .forms import CartAddProductForm
from .forms import CartAddProductForm_pz
from decimal import Decimal


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Prodotti, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=str(cd['quantity']),
                 override_quantity=cd['override'])

    next = request.POST.get('next', '/')
    print (next)

    if "/" in next:
        print ("Found!")
    else:
        print ("Not found!")
        next="/"

    return HttpResponseRedirect(next)


@require_POST
def cart_add_pz(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Prodotti, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add_pz(product=product,
                 quantity_pz=str(cd['quantity']),
                 override_quantity=cd['override'])
    #return redirect('cart:cart_detail')
    next = request.POST.get('next', '/')

    if "/" in next:
        print ("Found!")
    else:
        print ("Not found!")
        next="/"

    return HttpResponseRedirect(next)


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Prodotti, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    print('step 1')

    #for item in cart:
        # item['update_quantity_form'] = CartAddProductForm(initial={'quantity': str(item['quantity']),
        #                                                            'override': False})
        #
        # item['update_quantity_form_pz'] = CartAddProductForm_pz(initial={'quantity': str(item['quantity_pz']),
        #                                                             'override': False})
        
    print('step 2')
    return render(request, 'cart/detail.html', {'cart': cart})
