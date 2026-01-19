from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_page, name='students'),
    path('api/students/', views.students_api),
    path('api/add-student/', views.add_student_api),
]
