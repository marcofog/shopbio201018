from django.urls import path
from . import views

app_name='store'

urlpatterns=[
    #path('',views.store, name="store"),
    #path('cart/', views.cart, name="cart"),
	#path('checkout/', views.checkout, name="checkout"),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/',views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
]
