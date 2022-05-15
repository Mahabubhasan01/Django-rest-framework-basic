from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from api.models import Student
from api.serializer import StudentSerializer

# Create your views here.
def student_list(request):
    
    student = Student.objects.all()
    serializer = StudentSerializer(student,many=True)

    """ json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json') """

    return JsonResponse(serializer.data,safe=False)

    # student query 
def student_detail(request,pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)


    """ json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json') """


    # above two line shortcut
    return JsonResponse(serializer.data)