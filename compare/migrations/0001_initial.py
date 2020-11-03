# Generated by Django 3.1.3 on 2020-11-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('label', models.CharField(max_length=200)),
                ('product_price', models.FloatField()),
            ],
        ),
    ]
