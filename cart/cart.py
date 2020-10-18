from decimal import Decimal
from django.conf import settings
from store.models import Prodotti


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Prodotti.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            #item['total_price'] = item['price'] * Decimal(item['quantity'])
            #item['total_price']=0
            item['total_price'] = Decimal( str( round( float(item['price']) * float(item['quantity']),2 ) ))
            print('tot di riga')
            print(item['total_price'])
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """

        # a=sum(float(item['quantity']) for item in self.cart.values())
        # print('totale '+str(a))
        #
        # #return sum(float(item['quantity']) for item in self.cart.values()) # il ciclo for si può fare solo sugli interi.... ma cosa sono i values qui???
        # return 1
        b=0
        for item in self.cart.values():
            b=b+1

        #print('totale '+str(a))
        #print ("oggetti "+ str(b))

        return b




    def add(self, product, quantity=1.0, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': str(0), 'price': str(product.prezzo_quantità),
                                    'quantity_pz': str(0), 'price_pz': str(product.prezzo_pezzi)
                                    ,'unità_misura':str(product.unità_misura)
                                    }
        if override_quantity:
            self.cart[product_id]['quantity'] = str(quantity)
        else:
            self.cart[product_id]['quantity'] = str(float(self.cart[product_id]['quantity'])+ float(quantity))
            print('ok')
        self.save()
        print('salvataggio ok')

    def add_pz(self, product, quantity_pz=1.0, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity_pz': str(0),
                                     'quantity': str(0), 'price': str(product.prezzo_quantità),
                                      'price_pz': str(product.prezzo_pezzi)
                                      ,'unità_misura':str(product.unità_misura)
                                      }
        if override_quantity:
            self.cart[product_id]['quantity_pz'] = str(quantity_pz)
        else:
            self.cart[product_id]['quantity_pz'] = str(float(self.cart[product_id]['quantity_pz'])+ float(quantity_pz))
            print('ok')
        self.save()
        print('salvataggio ok')



    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        print('prova totale...')
        return sum(float(item['price']) * float(item['quantity']) for item in self.cart.values())
