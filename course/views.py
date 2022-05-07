from django.shortcuts import render
from django.http import HttpResponse
from course.models import Course , Departman
from django.contrib.auth.decorators import login_required

@login_required(login_url='/user/login/')
def course_list(request):
    queryset = Course.objects.all()
    return render(request,'course_list.html' , {'course_list' : queryset})

@login_required(login_url='/user/login/')
def departman_list(request):
    queryset = Departman.objects.all()
    return render(request , 'departman_list.html' , {'departman_list':queryset})
# Create your views here.


@login_required(login_url='/user/login/')
def course_department(request , pk):
    queryset = Course.objects.filter(department = pk)
    return render(request , 'course_list.html' , {'course_list':queryset})