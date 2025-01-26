from django import forms
from categories.models import Category


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'}
    ))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(
        attrs={'class':'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'}
    ))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(
        attrs={'class':'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'}
    ))
    description = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={'class':'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'}
    ))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class':'mt-1 block w-full'}
    ))

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be a positive value.")
        return price

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Product name is too short.')
        return name