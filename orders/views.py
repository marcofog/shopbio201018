from django.shortcuts import render
from .models import Ordini_dettaglio
from store.models import CostoConsegna, OrarioConsegna
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import send_mail
from shopbio_v1.settings import EMAIL_HOST_USER

# Create your views here.

def order_create(request):
    cart = Cart(request)
    costo_consegna=CostoConsegna.objects.all()
    orario_consegna=OrarioConsegna.objects.all()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            print(cart)
            num_ordine=order
            messaggio="Ciao "+str(form['nome'].value()).capitalize()+",\n"
            messaggio=messaggio+"Ecco il tuo ordine numero "+str(order)+":\n"

            # print(order)
            # print(" form")
            # print(form)
            #messaggio=""

            for item in cart:
                Ordini_dettaglio.objects.create(id_ordine=order,nome_prodotto=item['product'],prezzo_quantità=item['price'],q_quantità=item['quantity']
                ,prezzo_pezzi=item['price_pz'], q_pezzi=item['quantity_pz'], unità_misura=item['unità_misura']
                )
                messaggio=messaggio+":: "+str(item['product'])+" quantità:"+str(item['quantity'])+" "+item['unità_misura']

                if int(item['quantity_pz'])>0:
                    messaggio=messaggio+";  pezzi:"+item["quantity_pz"]+"\n"
                else:
                    messaggio=messaggio+"\n"

            # clear the cart
            cart.clear()



            # invio mail
            #sub = forms.Subscribe(request.POST)
            subject = 'Il tuo ordine di Cascina di Francia'
            #message = 'Hope you are enjoying your Django Tutorials'
            recepient = str(form['email'].value())
            send_mail(subject,messaggio, EMAIL_HOST_USER, [recepient], fail_silently = False)


            return render(request,'orders/order/created.html',{'order': order})
    else:
        form = OrderCreateForm()
        return render(request,'orders/order/create.html',{'cart': cart, 'form': form, 'costo_consegna':costo_consegna, 'orario_consegna':orario_consegna})
