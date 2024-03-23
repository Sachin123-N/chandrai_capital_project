from django import forms
from .models import Flat


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = "__all__"

        widgets = {
            "flat_owner_name": forms.TextInput(attrs={'class': 'class-controls'}),
            "flat_price": forms.NumberInput(attrs={'class': 'class-controls'}),
            "flat_no": forms.NumberInput(attrs={'class': 'class-controls'}),
            "maintaince_price": forms.NumberInput(attrs={'class': 'class-controls'}),
            "payment_mode": forms.Select(attrs={'class': 'class-controls'}),
            "room_quantity": forms.Select(attrs={'class': 'class-controls'}),
        }
