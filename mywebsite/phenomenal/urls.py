from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page),
    path('about', about),
    path('product', product),
    path('blog/<int:id>', post_detail),
    path('contact', contact),
    path('search', search),
    path('add-book', add_book),
    path('sign-in', sign_in),
    path('sign-out', sign_out),
]
