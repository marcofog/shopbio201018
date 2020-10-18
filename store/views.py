from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
import datetime
from .models import *
from cart.forms import CartAddProductForm
from cart.forms import CartAddProductForm_pz
from cart.cart import Cart # import carello


# Create your views here.

#...................................

def product_list(request,category_slug=None):
    category=None
    categories=Categoria.objects.all()
    products=Prodotti.objects.filter(disponibile=True)
    parametri=Parametri.objects.all()
    if category_slug:
        category=get_object_or_404(Categoria, slug=category_slug)
        products=products.filter(categoria=category)
    return render(request,
                'store/list.html',
                {'category':category,
                'categories':categories,
                'products':products,
                'parametri':parametri
                })

def product_detail(request, id, slug):
    cart = Cart(request)
    product=get_object_or_404(Prodotti,
                            id=id,
                            slug=slug,
                            disponibile=True)

    #q_ini=cart['id'==id]['quantity']
    q_ini=0
    q_ini_pz=0
    for item in cart:
        if item['product']==product:
            q_ini=item['quantity']
            q_ini_pz=item['quantity_pz']

    cart_product_form=CartAddProductForm(initial={'quantity': str(q_ini),'override': True})
    cart_product_form_pz=CartAddProductForm_pz(initial={'quantity': str(q_ini_pz),'override': True})

    return render(request,'store/detail.html',
                {'product':product,
                'cart_product_form':cart_product_form,
                'cart_product_form_pz':cart_product_form_pz,
                'cart': cart})
