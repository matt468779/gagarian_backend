# Generated by Django 3.2.10 on 2021-12-30 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20211230_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.products'),
        ),
    ]