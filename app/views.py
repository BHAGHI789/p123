from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from django.http import HttpResponse

@api_view(["GET"])
def Student_get(request):
    stud=Student.objects.all()
    serializer=StudentSerializer(stud,many=True)
    return Response(serializer.data)
@api_view(["GET"])
def student_get_1(request,pk):
    stud=Student.objects.get(id=pk)
    serializer=StudentSerializer(stud)
    return Response(serializer.data)


@api_view(["POST"])
def student_post(request):
    stud=Student.objects.all()
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def student_delete(request,pk):
    stud=Student.objects.get(id=pk)
    stud.delete()
    return Response("delete")

