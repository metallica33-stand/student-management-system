from django.http import JsonResponse
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
import json

def students_api(request):
    if request.method == 'GET':
        students = list(CustomUser.objects.values('username', 'role'))
        return JsonResponse(students, safe=False)

@csrf_exempt
def add_student_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = CustomUser.objects.create(
            username=data['username'],
            role='student'
        )
        return JsonResponse({'status': 'created'})
from django.shortcuts import render

def students_page(request):
    students = CustomUser.objects.filter(role='student')
    return render(request, 'core/students.html', {'students': students})
