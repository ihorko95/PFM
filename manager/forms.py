from django.core.exceptions import ValidationError

from .models import *
from django import forms

# class CreateTrans(forms.Form):
#     title = forms.CharField(max_length=80, label='Name')
#     slug = forms.SlugField(max_length=80, label='URL')
#     category = forms.ModelChoiceField(queryset=Categories.objects.all(),empty_label='Not selected')
#     description =forms.Textarea(attrs={'rows':60,'cols':40})
#     total =forms.DecimalField(decimal_places=2,label='Price',initial=0)
class CreateTrans(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
        #super().__init__(self, *args, **kwargs)
        #self.fields['category'].empty_label = 'Not selected'
    class Meta:
        model =Transactions
        #fields = '__all__'
        fields = ['title', 'slug', 'category', 'description', 'total']
        widgets = {
            'description': forms.Textarea(attrs={'rows':5,'cols':40}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title)<3:
            raise ValidationError('Title lenth less 3 simbols')
        return title
