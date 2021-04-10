from django.forms import ModelForm
from .models import Product
from .models import Customer
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ['name', 'price']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

