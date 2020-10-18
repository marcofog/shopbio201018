from django import forms
from .models import Ordini
from store.models import OrarioConsegna
from django.forms import ModelChoiceField

# class OrderCreateForm(forms.ModelForm):
#     class Meta:
#         model = Ordini
#         fields = ['nome', 'cognome', 'email', 'indirizzo','cap', 'città','telefono','orario_consegna','note']


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Ordini
        fields = ['nome', 'cognome', 'email', 'indirizzo','cap', 'città','telefono','orario_consegna','note']


    nome=forms.CharField()
    cognome=forms.CharField()
    email=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    indirizzo=forms.CharField()
    cap=forms.CharField()
    città=forms.CharField()
    telefono=forms.CharField()
    orario_consegna=forms.ModelChoiceField(queryset=OrarioConsegna.objects.all())
    note=forms.CharField(widget=forms.Textarea, required=False)
