import io

from django.shortcuts import render
from .models import student
from .serializer import StudentSerial
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def getstudent(request):

    # 1. This is work with objects.get function

    # obj=student.objects.get(id=1)
    # stu=StudentSerial(obj)
    # json_data=JSONRenderer().render(stu.data)
    # return HttpResponse(json_data,content_type='application/json')

    # 2.This is work with objects.all() function

    # obj=student.objects.all()
    # stu=StudentSerial(obj,many=True)
    # json_data=JSONRenderer().render(stu.data)
    # return HttpResponse(json_data,content_type='application/json')

    # 3. This is work with objcets.filter() function

    # obj=student.objects.filter(name='Daljit Singh')
    # stu=StudentSerial(obj,many=True)
    # json_data=JSONRenderer().render(stu.data)
    # return HttpResponse(json_data,content_type='application/json')

    # 4.
    obj=student.objects.all()
    stu=StudentSerial(obj,many=True)
    return JsonResponse(stu.data,safe=False)

@csrf_exempt
def savedata(request):
    if request.method=='POST':
        json_data=request.body
        print(json_data)
        print(type(json_data))
        stream=io.BytesIO(json_data)
        print(json_data)
        print(type(json_data))
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerial(data=pythondata)
        # serializer.Is_valid() it is use for boolen
        # serializer.error()
        # serializer.validate data
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Record Saved'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors,safe=False)


@csrf_exempt
def alldata(request):
    if request.method=='GET':
        json_data=request.body # this is use for get data
        stream=io.BytesIO(json_data) # this is use for store data in valriable
        python_data=JSONParser().parse(stream) # this is convert into python data type
        id=python_data.get('id')
        if id is not None:
            try:
                obj=student.objects.get(id=id)
            except:
                res={'message':'No Data Found'}
                return JsonResponse(res)
            stu=StudentSerial(obj)
            return JsonResponse(stu.data)
        else:
            obj=student.objects.all()
            stu=StudentSerial(obj,many=True)
            return JsonResponse(stu.data,safe=False)

    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerial(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'mes':'Data Saved'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors,safe=False)

    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        print(python_data)
        cspk=list(python_data.keys())
        cspk=cspk.remove('id')
        id=python_data.get('id')
        try:
            stu=student.objects.get(id=id)
        except:
            res={'msg':'Incorrect Information'}
            return JsonResponse(res)
        sspk=StudentSerial(stu)
        sspk=sspk.data
        sspk=list(sspk.keys())
        if sspk==cspk:
            serializer=StudentSerial(stu,data=python_data,partial=False)
        else:
            serializer = StudentSerial(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Record Updated'}
            return JsonResponse(res)
        else:
            return JsonResponse(serializer.errors,safe=False)



