from django.contrib import admin
from .models import Ordini, Ordini_dettaglio


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = Ordini_dettaglio
    raw_id_fields = ['nome_prodotto']

@admin.register(Ordini)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cognome', 'email',
    'indirizzo', 'cap', 'città', 'gestito',
    'created', 'updated']
    list_filter = ['gestito', 'created', 'updated']
    inlines = [OrderItemInline]
