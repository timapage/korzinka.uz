from products.models import *

# product jadvalidagi barcha ma'lumotlarni olish so'rovi
products = Product.objects.all()

# birinchi va oxirgi elementni qaytarish
firstProduct = Product.objects.first()
lastProduct = Product.objects.last()

# get() metodi orqali atribut qiymatlari bo'yicha ma'lumotlarni olish so'rovi

product = Product.objects.get(id=2)
product = Product.objects.get(productCode="P001")

# Bog'langan jadvallardan ma'lumot olish
# alex ga tegishli buyurtmalarni olish
customer = Customer.objects.get(name="Alex")
alexOrders = customer.orders_set.all()

# orders jadvalidagi "Order101" buyurtmasi kimga tegishli ekanligini aniqlash
order = Orders.objects.get(orderCode="Order101")
orderOwner = order.customer.name

# statusi "canceled" bo'lgan buyurtmalarni chiqarish
canceled = Status.objects.get(name="canceled").id
canceledOrders = Orders.objects.filter(status=canceled) #QuerySet qaytaradi
canceledOrders = Orders.objects.get(status=canceled) #Model obyektini qaytaradi

# ko'pga ko'p bog'langan jadvaldagi ma'lumotlarni olish
# Order102 nomli buyurtmaga tegishli mahsulotlarni chiqarish
order102Products = Product.objects.filter(orders__orderCode="Order102")

# Coca-cola nomli mahsulotga tegishli buyurtmalarni chiqarish
cocacolaOrders = Orders.objects.filter(products__name="Coca-cola")

# Category jadvaliga yangi ma'lumot qo'shish

newItem = Category(name="Milks", description="Milks products")
newItem.save()

# Category jadvaliga o'zgartirish kiritish
category = Category.objects.get(name="Milks")
category.description = "Different Milk products category"

category.save()

# Category jadvalidan elementni o'chirish
category = Category.objects.get(id=4)
category.delete()


