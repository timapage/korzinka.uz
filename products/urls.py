from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', views.ProductViewset ,basename='product')

urlpatterns = [
    #api urls
    path('viewset/', include(router.urls)),

    #template urls
    path('', views.homepage, name="home"),
    path('products/', views.products, name="products"),
    path('customers/', views.customers, name="customers"),
    path('category/<str:cid>/', views.categories, name="category"),

    # path('create_products', views.createProduct, name="create_products"),
    
    path('create_products/<str:cid>', views.createProduct, name="create_products"),
    path('update_products/<str:pid>', views.updateProduct, name="update_products"),
    path('delete_products/<str:pid>', views.deleteProduct, name="delete_products"),

    path('create_customer', views.createCustomer, name='create_customer'),
    path('update_customer/<str:cid>', views.updateCustomer, name='update_customer'),
    path('delete_customer/<str:cid>', views.deleteCustomer, name='delete_customer'),

    path('create_category', views.createCategory, name='create_category'),

    path('registrationpage/', views.userRegistration, name='registrationpage'),
    path('loginpage/', views.userLogin, name='loginpage'),
    path('logoutuser/', views.userLogout, name='logoutuser'),

    path('userprofile/', views.userProfile, name='userprofile'),
    path('profilesettings/', views.profileSettings, name='profilesettings'),


]

