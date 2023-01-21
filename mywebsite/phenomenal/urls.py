from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page),
    path('about', about),
    path('product', product),
    path('blog/<int:id>', post_detail),
]
