from django.contrib import admin

# Register your models here.

from myapp.models import Member

admin.site.register(Member)