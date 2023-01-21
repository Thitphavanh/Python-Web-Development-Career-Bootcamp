from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home_page(request):
    # variable = Table.objects.method()
    # Query all posts
    all_posts = Post.objects.all()
    context = {"all_posts": all_posts}
    return render(request, "phenomenal/home.html", context)


def post_detail(request, id):
    # Query 1 post
    single_post = Post.objects.get(id=id)
    context = {"single_post": single_post}
    return render(request, "phenomenal/post-detail.html", context)


def about(request):
    all_products = Product.objects.all()
    context = {"all_products": all_products}
    return render(request, "phenomenal/about.html", context)


def product(request):
    all_products = Product.objects.all()
    context = {"all_products": all_products}
    return render(request, "phenomenal/product.html", context)
