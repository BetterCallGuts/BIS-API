from django.contrib import admin

# Register your models here.
from .models  import Parent, Account



admin.site.register([Parent, Account])