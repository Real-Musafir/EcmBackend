# Generated by Django 3.1.4 on 2021-02-06 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=50)),
                ('active', models.BooleanField(default=True)),
                ('ordered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, null=True)),
                ('line_item_total', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.cart')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(through='carts.CartItem', to='products.Product'),
        ),
    ]
