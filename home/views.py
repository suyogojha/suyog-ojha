from django.shortcuts import redirect, render,reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.


# for home
def home(request):
    mimg = myprofilepic.objects.all()
    context = {
        "mimg": mimg,      
     
        }
    return render(request, "index.html", context)

# redirect to about us
def about(request):
    data = myskillsabout.objects.all()
    myimg = myprofilepic.objects.all()

    context = {
        "data": data, 
        "myimg": myimg,      
     
        }
    return render(request, "about.html",  context)

def Extra(request):
    return render(request, "Extra.html")


# redirect to portfolio
def portfolio(request):
    data = myportfilio.objects.all()
    context = {"data": data}
    return render(request, "portfolio.html", context)


def contact_us(request):
    if request.method =='POST':
        contact = contactus()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
    return render(request, 'contact_us.html')


def blog(request):
    data = myblog.objects.all()
    context = {"data": data}
    return render(request, "blog.html", context)


def blog_post(request,slug):
    newblog = myblog.objects.get(new_slug=slug)
    context = {
        "newblog": newblog,
        }
    return render(request, "blog_post.html", context)


