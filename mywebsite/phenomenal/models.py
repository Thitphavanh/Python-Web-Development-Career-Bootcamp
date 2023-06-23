from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=160)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    featured_pic = models.ImageField(upload_to="cover/", null=True, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True)
    price = models.FloatField(default=1000)
    instock = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    sender = models.CharField(max_length=80)
    detail = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=1000)

    def __str__(self):
        return f"{self.title} ({self.price})"
