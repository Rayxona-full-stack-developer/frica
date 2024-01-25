from django.db import models
from django.urls import reverse
# Create your models here.
class Categary(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='image/')
    email = models.EmailField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='image/')
    email = models.EmailField()

    def __str__(self):
        return self.name


class Mansclothes (models.Model):
    bio = models.TextField()
    img = models.ImageField(upload_to='image/')
    status = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100)

    def get_absolute_url(self):
        return reverse('manDetail', args=[self.slug])

    def __str__(self):
        return self.name


class Womanclothes(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='image/')
    bio = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=200)
    number = models.IntegerField()
    massage = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Computers(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='image/')
    slug = models.SlugField(max_length=300)
    status = models.TextField()
    # def get_absolute_url(self):
    #     return rewerse
    #
    # rayxonaolimjonova6 @ gmail.com

    def __str__(self):
        return self.name