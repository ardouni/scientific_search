from django.contrib import admin
from django.contrib import admin
from .models import ScientificPaper

class ScientificPaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'keywords')

admin.site.register(ScientificPaper, ScientificPaperAdmin)

# Register your models here.
