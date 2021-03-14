from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import PhoneBook
from django.contrib.auth import get_user_model

User = get_user_model()



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class AddUserForm(ModelForm):
    class Meta:
        model = PhoneBook
        fields = '__all__'
        
       