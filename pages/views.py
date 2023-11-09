from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def testimonial(request):
    return render(request, 'pages/testimonial.html')

def activities(request):
    return render(request, 'pages/activities.html')

def blog(request):
    return render(request, 'pages/blog.html')

def gallery(request):
    return render(request, 'pages/gallery.html')