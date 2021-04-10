# Generated by Django 3.1.7 on 2021-03-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210313_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitems',
            old_name='orderCode',
            new_name='order',
        ),
        migrations.RemoveField(
            model_name='orderitems',
            name='products',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
