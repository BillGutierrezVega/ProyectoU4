from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from login.models import FormProyecto


class UserLoginForm(forms.Form):
    user_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    


class FormProyectoForm(forms.ModelForm):
    class Meta:
        model = FormProyecto
        fields = ['foto','titulo_proyecto','description_proyecto','tags','url_github']
        
        
class FormularioUsusariCustom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']