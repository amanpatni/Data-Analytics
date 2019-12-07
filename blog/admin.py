from django.contrib import admin

# Register your models here.
# .refers to the current directory eg : .models

from .models import Blog

admin.site.register(Blog)
