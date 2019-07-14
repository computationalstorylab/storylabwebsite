from django.db import models

class Author(models.Model):
    def __str__(self):
        return self.fullname
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200,default='Smarty McPants')
    position = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

class Paper(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200,default='Fire Research')
    authors = models.CharField(max_length=200)
    abstract = models.IntegerField(default=0)
    body = models.IntegerField(default=0)
    citations = models.IntegerField(default=0)
    journal = models.IntegerField(default=0)
    pubdate = models.IntegerField(default=0)
    link = models.IntegerField(default=0)
    
class OnlineAppendices(models.Model):
    def __str__(self):
        return self.associatedpaper
    associatedpaper = models.CharField(max_length=200,default='Extra Goodness')
    body = models.CharField(max_length=200)
    images = models.IntegerField(default=0)
    