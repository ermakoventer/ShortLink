from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя:',
        required=True,
        help_text = 'Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя','autocomplete':'off' })
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Введите Email', 'autocomplete':'off'})
)
    password1 = forms.CharField(
        label='Пароль',
        required=True,
        help_text = 'Пароль не должен быть маленьким и простым',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'autocomplete':'off'})
        )


    class Meta:
        model = User
        fields = ['username','email', 'password1',]
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Введите Логин',
        required=True,
        help_text = 'Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Логин'})
    )
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )

    class Meta:
        model = User
        fields = ['username','email']

    
# class Url(forms.ModelForm):
#     url = forms.CharField(label='Длинная ссылка:', required=True)
#     slug = forms.CharField(label='Сокращенная ссылка:', required=True)

#     class Meta:
#         model = UrlData
#         fields = ['url', 'slug']