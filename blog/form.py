from django import forms
from django.contrib.auth.forms import UserCreationForm,authenticate
from django.contrib.auth.models import User
from .models import Post
class RegisterForm(UserCreationForm):
   

    class Meta:
        model=User
        fields = ["username", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı adını veya şifreyi yanlış girdiniz!")
        return super(LoginForm, self).clean()
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        
        fields=["title","text"]