# Generated by Django 5.1.4 on 2025-02-01 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagement', '0003_contact_alter_product_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
    ]
