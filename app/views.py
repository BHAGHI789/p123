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


"""@api_view(["GET"])
def student_get_1(request, name):
    try:
        stud = Student.objects.get(name=name)
    except Student.DoesNotExist:
        return Response({'message': 'Student not found'}, status=404)

    serializer = StudentSerializer(stud)
    return Response(serializer.data)"""

@api_view(["POST"])
def student_post(request):
    stud=Student.objects.all()
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["PUT"])
def student_patch(request, pk):
    try:
        stud = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({'message': 'Student not found'}, status=404)

    serializer = StudentSerializer(instance=stud, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
@api_view(["DELETE"])
def student_delete(request,pk):
    stud=Student.objects.get(id=pk)
    stud.delete()
    return Response("delete")

"""@api_view(["PUT"])
def student_patch(request,pk):
    stud=Student.objects.get(id=pk)
    serializer=StudentSerializer(instance=stud,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)"""