from django.shortcuts import render
from stud_app.models import Student
from django.views.generic import View
# Create your views here.

# create

class Createstudentview(View):
    def get(self,request):
        return render(request,"student_form.html")
    
    def post(self,request):
        print(request.POST)
        Student.objects.create(name=request.POST.get('name'),
                               email=request.POST.get('email'),
                               age=request.POST.get('age'),
                               course=request.POST.get('course'))
        return render(request,"student_form.html")

# read

class Readstudentview(View):
    def get(self,request):
        data = Student.objects.all()
        return render(request,"student_list.html",{'data':data})