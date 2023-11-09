from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('activities', views.activities, name='activities'),
    path('gallery', views.gallery, name='gallery'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('blog', views.blog, name='blog'),
]

