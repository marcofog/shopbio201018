from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(
    #                             choices=PRODUCT_QUANTITY_CHOICES,
    #                             coerce=int)

    quantity = forms.CharField(widget= forms.NumberInput(attrs={'id':'number','step': 0.1, 'style':'max-width:56px;'})
                                , label=""
                                )
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)


class CartAddProductForm_pz(forms.Form):
    quantity = forms.CharField(widget= forms.NumberInput(attrs={'id':'number_pz','style':'max-width:56px;'})
                                , label=""
                                )
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
