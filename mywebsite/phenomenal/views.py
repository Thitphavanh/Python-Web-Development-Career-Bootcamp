from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home_page(request):
    # variable = Table.objects.method()
    # Query all posts
    all_posts = Post.objects.all()

    return render(request, "phenomenal/home.html", {"all_posts": all_posts})


def about(request):
    return render(request, "phenomenal/about.html")
