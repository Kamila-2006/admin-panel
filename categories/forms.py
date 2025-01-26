from django import forms


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'class':'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
        }
    ))
    description = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={
            'class':'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
        }
    ))
    icon = forms.ImageField(widget=forms.FileInput(
        attrs={
            'class':'mt-1 block w-full'
        }
    ))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Category name is too short.')
        return name