from __future__ import unicode_literals
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=600, default='type')
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class Catalogue(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=600, default='type')
    price = models.CharField(max_length=600, default='type')
    description = models.TextField(max_length=600, null=True, blank=True)
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class About(models.Model):
    paragraph = models.CharField(max_length=600, default='type')
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class Cooperation(models.Model):
    paragraph = models.CharField(max_length=600, default='type')

    def __str__(self):
        return self.paragraph


class Brand(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=600, default='type')
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=600, default='type')
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class Map(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=600, default='type')
    address = models.CharField(max_length=600, default='type')
    phone = models.CharField(max_length=600, default='type')
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=200)
    phone = models.CharField(max_length=600, default='type')
    email = models.CharField(max_length=600, default='type')
    num = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class SubMenu(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
