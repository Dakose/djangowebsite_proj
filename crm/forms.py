from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

