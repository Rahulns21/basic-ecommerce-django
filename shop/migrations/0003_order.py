# Generated by Django 5.0.1 on 2024-01-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_options_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.PositiveIntegerField(max_length=12)),
                ('address', models.TextField(max_length=1000)),
            ],
        ),
    ]
