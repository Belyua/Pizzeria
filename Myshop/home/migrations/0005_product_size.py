# Generated by Django 4.1.4 on 2022-12-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_productcustomfield_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=4, null=True),
        ),
    ]