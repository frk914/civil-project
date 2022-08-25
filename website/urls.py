from django.urls import path
from . import views
app_name = 'website'


urlpatterns = [
    path('', views.home , name='home'),

    path('detail/<int:pk>/', views.ProjDetailView.as_view(), name='detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    
    path('contact/', views.contact_form, name='contact'),
    path('project/', views.Project.as_view(), name='project'),
    path('career/', views.Career.as_view(), name='career' ),
    path('our-blog/', views.OurBlog.as_view(), name='our-blog'),

    path('blog_details/<int:pk>/', views.BlogDetails.as_view(), name='blog_details'),

   

  
]