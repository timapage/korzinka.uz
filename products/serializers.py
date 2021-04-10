from rest_framework import serializers
from .models import Product, Category, Customer, Status, Orders

class ProductSerializer(serializers.ModelSerializer):
    class  Meta:
        model=Product
        # fields = ['id','title','author']
        fields = '__all__'

    
    

