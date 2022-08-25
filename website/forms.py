from django import forms
from django.forms import ModelForm
from .models import  ContactForm, Comment

class MyForm(forms.ModelForm):
     class Meta:
         model = ContactForm
         fields = '__all__'

         widgets = {
             'name': forms.TextInput(attrs={'placeholder':'Enter your name'}),
             'phone_number': forms.NumberInput(attrs={'placeholder':'Enter your phone number'}),
             'email': forms.EmailInput(attrs={'placeholder':'Enter your email'}),
             'subject': forms.Textarea(attrs={'placeholder':'Send your query...'}),
         }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')