# Generated by Django 3.2.6 on 2021-12-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='seller',
            field=models.BooleanField(default=False, null=True),
        ),
    ]