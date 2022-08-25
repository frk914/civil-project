from django.contrib import admin
from .models import  Blog, Product, ContactForm, Comment 

admin.site.register([Product,ContactForm, Blog, Comment])
