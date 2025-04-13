from django.contrib import admin
from .models import Chapel, Session, Student

# Register your models here.
admin.site.register(Chapel)
admin.site.register(Session)
admin.site.register(Student)