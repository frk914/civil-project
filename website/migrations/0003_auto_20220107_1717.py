# Generated by Django 3.1.7 on 2022-01-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='complete_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='emp_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
