# Generated by Django 3.1.7 on 2021-04-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profilePicture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
