from pyexpat import model
from django import forms
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/', blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    emp_number = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateField(null=True,blank=True)
    complete_date = models.DateField(null=True,blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='media/', blank=True)
    author = models.CharField(max_length=100)
    blog_desc = models.TextField()
    create = models.DateField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)