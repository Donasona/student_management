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
    
# update

class Updatestudentview(View):
    def get(self,request,**kwargs):
        update_id=kwargs.get("pk")
        student_data=Student.objects.get(id=update_id)
        return render(request,"student_update.html",{"student_data":student_data})
    
    def post(self,request,**kwargs):
        update_id=kwargs.get("pk")
        student_data=Student.objects.get(id=update_id)
        print(request.POST)
        student_data.name=request.POST.get("name")
        student_data.email=request.POST.get("email")
        student_data.age=request.POST.get("age")
        student_data.course=request.POST.get("course")
        student_data.save()
        return render(request,"student_update.html")

class Deletestudentview(View):
    def get(self,request,**kwargs):
        delete_id=kwargs.get("pk")
        Student_data=Student.objects.get(id=delete_id)
        Student_data.delete()
        return render(request,"student_form.html")       



