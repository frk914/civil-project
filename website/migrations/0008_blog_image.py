# Generated by Django 3.1.7 on 2022-01-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
