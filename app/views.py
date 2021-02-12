from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_api(request):

    if (request.method== "GET"):
        json_data= request.body
        stream= io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

    if(request.method=="POST"):
        json_data= request.body
        stream= io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        serializer= StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res= {'msg':"Data created successfully"}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        return HttpResponse(JSONRenderer.render(serializer.errors), content_type='application/json')

    if(request.method == "PUT"):
        json_data= request.body
        stream= io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id= id)
            serializer = StudentSerializer(stu, data=python_data)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': "Data updated successfully"}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            res = {'msg':"Data not valid"}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        res = {'msg': "Data not valid"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')


    if(request.method== "DELETE"):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            try:
                stu = Student.objects.get(id= id)
            except Student.DoesNotExist:
                res = {'msg': "Student with this id does not exist"}
                json_data= JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            stu.delete()
            res = {'msg': "Student has been deleted successfully"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        res = {'msg': "Please provide some id to delete the student"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')

  # stu = Student.objects.get(roll=2)
    # serializer = StudentSerializer(stu)
    # json_data= JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data= request.body
        stream= io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        serializer= StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res= {'msg':"Data created successfully"}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        return HttpResponse(JSONRenderer().render(serializer.errors), content_type='application/json')