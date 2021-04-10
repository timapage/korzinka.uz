from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from django.http import HttpResponse
from .models import *

from .forms import ProductForm
from .forms import CustomerForm
from .forms import CategoryForm

from .filters import ProductFilter

# from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import unathenticated_user, allowed_users, admin_only


from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404



class ProductViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, 
                mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductViewset2(viewsets.ViewSet):
    def list(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset,pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self,request, pk=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@login_required(login_url="loginpage")
# @allowed_users(allowed_users=["admin"])
@admin_only
def homepage(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    pfilter = ProductFilter(request.GET, queryset=products)
    products = pfilter.qs

    context = {'categories': categories, 'products': products, 
                'pfilter': pfilter}
    return render(
        request, 
        'products/homepage.html', 
        context)

def products(request):
    products = Product.objects.all()
    return render(
        request, 
        'products/products.html', 
        {'products': products})

# def createProduct(request):
#     myform = ProductForm()

#     if request.method == 'POST':
#         print("POST result in Terminal:", request.POST)
#         myform = ProductForm(request.POST)
#         if myform.is_valid():
#             myform.save()
#             return redirect('products/')
#     context = {'myform': myform}
#     return render(request, 'products/product_form.html', context)

def createProduct(request, cid):
    MyFormSet = inlineformset_factory(Category, Product, 
                                    fields = ('name', 'productCode', 'price'), extra=5)
    category = Category.objects.get(id=cid)

    # formset = MyFormSet(instance=category)
    formset = MyFormSet(queryset = Product.objects.none(), instance=category)

    #myform = ProductForm(initial={'category': category})

    if request.method == 'POST':
        print("POST result in Terminal:", request.POST)
        # myform = ProductForm(request.POST)
        formset = MyFormSet(request.POST, instance=category)
        if formset.is_valid():
            formset.save()
            return redirect('/products')
    context = {'formset': formset}
    return render(request, 'products/product_form.html', context)

def updateProduct(request, pid):
    product = Product.objects.get(id=pid)
    myform = ProductForm(instance=product)

    if request.method == 'POST':
        myform = ProductForm(request.POST, instance=product)
        if myform.is_valid():
            myform.save()
            return redirect('/')
    context = {'myform': myform}
    return render(request, 'products/product_form.html', context)

def deleteProduct(request, pid):
    product = Product.objects.get(id=pid)
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    context = {"item": product}
    return render(request, 'products/product_delete.html', context)

def customers(request):
    customers = Customer.objects.all()
    data = {'customers': customers}
    return render(request, 'products/customers.html', data)


def createCustomer(request):
    customerForm = CustomerForm()

    if request.method == "POST":
        mycustomer = CustomerForm(request.POST)
        if mycustomer.is_valid():
            mycustomer.save()
            return redirect('customers/')

    form = {'customerForm': customerForm}
    return render(request, 'products/customer_form.html', form)

def updateCustomer(request, cid):
    customer = Customer.objects.get(id=cid)
    customerForm = CustomerForm(instance=customer)

    if request.method == "POST":
        mycustomer = CustomerForm(request.POST, instance=customer)
        if mycustomer.is_valid():
            mycustomer.save()
            return redirect('/customers')

    form = {'customerForm': customerForm}
    return render(request, 'products/customer_form.html', form)

def deleteCustomer(request, cid):
    customer = Customer.objects.get(id=cid)

    if request.method == 'POST':
        customer.delete()
        return redirect('/customers')

    data = {'item': customer}
    return render(request, 'products/customer_delete.html', data)

def categories(request, cid):
    category = Category.objects.get(id=cid)
    number_of_products = category.product_set.all().count()
    products = category.product_set.all()
    return render(
        request, 
        'products/categories.html', 
        {'category': category, 'number_of_products': number_of_products, 'products': products})


def createCategory(request):
    categoryForm = CategoryForm()

    if request.method == "POST":
        categoryForm = CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('/')

    form = {'categoryForm': categoryForm}
    return render(request, 'products/category_form.html', form)

@unathenticated_user
def userRegistration(request):
    userform = UserForm()

    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            user = userform.save()

            guest = Group.objects.get(name='guest')
            user.groups.add(guest) 

            return redirect('loginpage')
    
    form = {'userform': userform}
    return render(request, 'products/registrationpage.html', form)


# @unathenticated_user
# def userRegistration(request):
#     userform = UserForm()
    
#     if request.method == 'POST':
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             userform.save()
#             return redirect('loginpage')
    
#     form = {'userform': userform}
#     return render(request, 'products/registrationpage.html', form)

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            passw = request.POST['password']
    
            myuser = authenticate(request, username=username, password=passw)
            if myuser is not None:
                login(request, myuser)
                return redirect('home')
            else:
                return redirect('registrationpage')

        return render(request, 'products/loginpage.html')


def userLogout(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url="loginpage")
def userProfile(request):
    orders = Orders.objects.all()
    products = Product.objects.all()

    userorders = request.user.customer.orders_set.all()
    context = {'userorders': userorders}
    return render(request, 'products/userprofile.html', context)


def profileSettings(request):
    user = request.user.customer
    form = CustomerForm(instance=user)
    successful_submit = False

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            successful_submit = True
            # return redirect('userprofile')

    context = {'form': form, 'successful_submit': successful_submit}
    return render(request, 
        'products/profilesettings.html', 
        context)


