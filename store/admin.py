from django.contrib import admin
from .models import Prodotti, Categoria, CostoConsegna, OrarioConsegna, Parametri

# Register your models here.
# admin.site.register(Prodotti)
# admin.site.register(Categoria)
# admin.site.register(Ordini)
# admin.site.register(Ordini_dettaglio)

@admin.register(Categoria)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['categoria','slug']
    prepopulated_fields={'slug':('categoria',)}

@admin.register(Prodotti)
class ProductAdmin(admin.ModelAdmin):
    list_display=['nome_prodotto','categoria', 'slug','prezzo_quantità', 'disponibile']
    list_filter=['disponibile','categoria']
    list_editable=[ 'slug','prezzo_quantità', 'disponibile']
    prepopulated_fields={'slug':('nome_prodotto',)}
    list_display_links = ['nome_prodotto']

@admin.register(CostoConsegna)
class CostoConsegnaAdmin(admin.ModelAdmin):
    list_display=['Località','Importo']

admin.site.register(OrarioConsegna)

#admin.site.register(Parametri)

@admin.register(Parametri)
class Parametri(admin.ModelAdmin):
    list_display=['Chiave','Valore']
