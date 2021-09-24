from django import forms
from .models import UrlData

class Url(forms.ModelForm):
    url = forms.CharField(label='Длинная ссылка:', required=True)
    slug = forms.CharField(label='Сокращенная ссылка:', required=True)

    class Meta:
        model = UrlData
        fields = ['url', 'slug']