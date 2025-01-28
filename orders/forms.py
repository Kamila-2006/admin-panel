from django import forms


class OrderForm(forms.Form):
    order_id = forms.CharField(max_length=10, widget=forms.TextInput(attrs={
        'readonly': 'readonly',
    }))
    date = forms.DateField(widget=forms.DateInput(
        attrs={
            'readonly': 'readonly',
            'class':'mt-1 block w-full border-gray-300 rounded-md shadow-sm'
        }
    ))
    status = forms.CharField(widget=forms.TextInput(
        attrs={
            'readonly': 'readonly',
            'class':'mt-1 block w-full border-gray-300 rounded-md shadow-sm'
        }
    ))

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'readonly': 'readonly',
        'class':'mt-1 block w-full border-gray-300 rounded-md shadow-sm'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'readonly': 'readonly',
        'class':'mt-1 block w-full border-gray-300 rounded-md shadow-sm'
    }))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'readonly': 'readonly',
        'class':'mt-1 block w-full border-gray-300 rounded-md shadow-sm'
    }))
    address = forms.CharField(widget=forms.Textarea(attrs={
        'readonly': 'readonly',
        'class':'mt-1 block w-full border-gray-300 rounded-md shadow-sm'
    }))

class OrderItemForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput(
        attrs={
            'readonly':'readonly'
        }
    ))
    product_id = forms.IntegerField(widget=forms.HiddenInput(
        attrs={
            'readonly': 'readonly'
        }
    ))
    product_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'readonly': 'readonly',
            'class': 'w-full border-gray-300 rounded-md shadow-sm'
        }
    ))
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(
        attrs={
            'readonly': 'readonly',
            'class': 'w-full border-gray-300 rounded-md shadow-sm'
        }))
    price = forms.DecimalField(widget=forms.NumberInput(
        attrs={
            'readonly': 'readonly',
            'class': 'w-full border-gray-300 rounded-md shadow-sm'
        }))
    total = forms.DecimalField(widget=forms.NumberInput(
        attrs={
            'readonly': 'readonly'
        }
    ))