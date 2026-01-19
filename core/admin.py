from django.contrib import admin
from .models import CustomUser, Subject, ClassRoom, Grade, StudentProfile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'email')
    search_fields = ('username', 'email')
    list_filter = ('role',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'score')
    list_filter = ('subject',)
