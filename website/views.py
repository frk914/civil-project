from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView 
from .models import Product, ContactForm, Blog, Comment
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import  MyForm, CommentForm

def home(request):
    product = Product.objects.all()[:3]
    return render(request, 'home.html', context={'product':product})


def contact_form(request):
      if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'form submit successsfully.')
            return HttpResponseRedirect('/')
        
      form = MyForm()
      return render(request, 'contact.html', context={'form':form})

class ProjDetailView(TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = kwargs['pk']
        product = Product.objects.get(pk=id)
        context['product'] = product
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

class Project(TemplateView):
    template_name = 'project.html' 


    def get_context_data(self, **kwargs):
         context =  super().get_context_data(**kwargs)
         all_products  = Product.objects.all().order_by('-id')
         paginator = Paginator(all_products,3)
         page_number = self.request.GET.get('page')
         product_list = paginator.get_page(page_number)
         context['product_list'] = product_list
         return context 

class Career(TemplateView):
    template_name = 'career.html'


class OurBlog(TemplateView):
    template_name = 'our-blog.html'

    
    def get_context_data(self, **kwargs):
         context =  super().get_context_data(**kwargs)
         context['blog_list']  = Blog.objects.all().order_by('-id')
         return context 

class BlogDetails(TemplateView):
    template_name = 'blog_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        blog = Blog.objects.get(pk=id)
        form = CommentForm()
        comments = blog.comment_set.all()
        context['blog'] = blog
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get(request)
        context = super().get_context_data(**kwargs)
        
        post = Blog.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                name=name, email=email, content=content, post=post
            )
            form = CommentForm()
            id = self.kwargs['pk']
            blog = Blog.objects.get(pk=id)
            context['blog'] = blog
            context['post'] = post
            context['form'] = form
            return render(request, 'blog_details.html', context=context)

        return self.render_to_response(context=context)


   