from django.shortcuts import render
from .models import *
import smtplib as smtp
# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

