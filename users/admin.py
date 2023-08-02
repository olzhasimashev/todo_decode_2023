from django.contrib import admin
from tasks.models import Task
from django.contrib.auth import get_user_model

# Register your models here.


# class AuthorAdmin(admin.ModelAdmin):
#     pass
admin.site.register(get_user_model())
admin.site.register(Task)