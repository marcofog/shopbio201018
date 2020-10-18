from django.db import models
from store.models import Prodotti


# Create your models here.
class Ordini (models.Model):
    nome=models.CharField(max_length=50)
    cognome=models.CharField(max_length=50)
    email=models.EmailField()
    indirizzo=models.CharField(max_length=100)
    cap=models.CharField(max_length=10)
    città=models.CharField(max_length=50)
    telefono=models.CharField(max_length=20)
    orario_consegna=models.CharField(max_length=50)
    #costo_consegna=models.CharField(max_length=50)
    note=models.TextField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    gestito=models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name="Ordini"
        verbose_name_plural="Ordini"


    def __str__(self):
        #return f'Order {self.id}'
        return str(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class Ordini_dettaglio (models.Model):
    id_ordine=models.ForeignKey(Ordini,on_delete=models.CASCADE,related_name='items')
    nome_prodotto = models.ForeignKey(Prodotti,related_name='order_items',on_delete=models.CASCADE)
    prezzo_pezzi=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    prezzo_quantità=models.DecimalField(max_digits=7, decimal_places=2)
    q_pezzi= models.PositiveIntegerField(default=1, null=True, blank=True)
    q_quantità=models.DecimalField(max_digits=7, decimal_places=2)
    unità_misura=models.CharField(max_length=10, null=True, blank=True)


    class Meta:
        verbose_name="Ordini Dettaglio"
        verbose_name_plural="Ordini Dettaglio"

    def __str__(self):
        #return str(self.id_ordine)+ '_'+str(self.pk)+'_'+self.nome_prodotto
        return str(self.id)

    def get_cost(self):
        return self.prezzo_quantità * self.q_quantità
