from __future__ import unicode_literals
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Catalogue(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Cooperation(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Map(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

