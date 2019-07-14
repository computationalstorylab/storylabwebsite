from django.contrib import admin

from .models import Author, Paper, OnlineAppendices

admin.site.register(Author)
admin.site.register(Paper)
admin.site.register(OnlineAppendices)