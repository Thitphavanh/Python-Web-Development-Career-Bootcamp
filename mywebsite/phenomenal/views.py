from django.shortcuts import *
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import *
from django.contrib import messages


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


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to DB
            form.save()
            return redirect("/")
        context = {"form": form}

    else:
        form = ContactForm()
        context = {"form": form}
    return render(request, "phenomenal/contact.html", context)


def search(request):
    # Get the incoming query params
    search_post = request.GET.get("q")
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post))
        context = {"posts": posts}
    else:
        context = {"posts": posts}
    return render(request, "phenomenal/search.html", context)


@login_required
def add_book(request):
    if request.method == "POST":
        data = request.POST.copy()
        book_title = data.get("book_title")
        book_description = data.get("book_description")
        book_price = data.get("book_price")

        new_book = Book()
        new_book.title = book_title
        new_book.description = book_description
        new_book.price = float(book_price)
        new_book.save()

    return render(request, "phenomenal/add-book.html")


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log user in
            login(request, user)
            return redirect("/")
        messages.error(request, 'Invalid Login')

    return render(request, "phenomenal/sign-in.html")


def sign_out(request):
    # Sign user out
    logout(request)
    return redirect("/sign-in")
