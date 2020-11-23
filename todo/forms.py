""" This is for Forms """
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    """ This is for Forms """
    class Meta:
        model = Item
        fields = ["name", "done"]
        