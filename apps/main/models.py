from django.db import models
from datetime import datetime

class Carousel(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    text = models.CharField(max_length=500, null=False, blank=False)
    photo = models.ImageField(upload_to='fotos', blank=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

class About(models.Model):
    photo = models.ImageField(upload_to='fotos', blank=True)
    title = models.CharField(max_length=100, null=False, default='null')
    text = models.CharField(max_length=1000, null=False, blank=False)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
    def set_default_title(self):
        return self.text[:20]

class Expertise(models.Model):
    photo = models.ImageField(upload_to='fotos', blank='False')
    title = models.CharField(max_length=100, null=False, default='null')
    text = models.CharField(max_length=1000, null=False, blank=False)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

class Appointment(models.Model):
    photo = models.ImageField(upload_to='fotos', blank='False')
    title = models.CharField(max_length=100, null=False, default='null')
    text = models.CharField(max_length=1000, null=False, blank=False)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

class Article(models.Model):
    photo = models.ImageField(upload_to='fotos', blank='False')
    title = models.CharField(max_length=100, null=False, default='null')
    sub_title = models.CharField(max_length=100, null=False, default='null')
    text = models.CharField(max_length=1500, null=False, blank=False)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title



