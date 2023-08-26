from django import forms
from .models import Contact

class ItemForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name1', 'name']

