# Generated by Django 3.1.7 on 2022-01-31 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]