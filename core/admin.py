from django.contrib import admin
from .models import CustomUser, Subject, ClassRoom, Grade, StudentProfile

admin.site.register(CustomUser)
admin.site.register(Subject)
admin.site.register(ClassRoom)
admin.site.register(Grade)
admin.site.register(StudentProfile)
