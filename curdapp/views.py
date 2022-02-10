from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from .models import studentsdata

def fetching_data(request):
    students=studentsdata.objects.all()
    return render(request,'fetching.html',{'student':students})


def adding_data(request):
    if request.method=='POST':
        studentsdata(
        first_name=request.POST.get('fname'),
        last_name=request.POST.get('lname'),
        course=request.POST.get('course'),
        fee=request.POST.get('fee'),
        assignment1=request.POST.get('a1'),
        assignment2=request.POST.get('a2'),
        assignment3=request.POST.get('a3'),
        assignment4=request.POST.get('a4'),
        Total=int(request.POST.get('a1'))+int(request.POST.get('a2'))+int(request.POST.get('a3'))+int(request.POST.get('a4')),
        Avg=(int(request.POST.get('a1'))+int(request.POST.get('a2'))+int(request.POST.get('a3'))+int(request.POST.get('a4')))/4
        ).save()
        return redirect('fetching')
    else:
        return render(request,'adding.html')


def update_data(request,id):
    if request.method=='POST':
         soumya=studentsdata.objects.get(id=id)
         soumya.first_name=request.POST.get('fname')
         soumya.last_name=request.POST.get('lname')
         soumya.course=request.POST.get('course')
         soumya.fee=request.POST.get('fee')
         soumya.assignment1=request.POST.get('a1')
         soumya.assignment2=request.POST.get('a2')
         soumya.assignment3=request.POST.get('a3')
         soumya.assignment4=request.POST.get('a4') 
         soumya.save()
         return redirect('fetching')
    else:
         student=studentsdata.objects.get(id=id)
         return render(request,'update.html',{'Student':student})



def delete_data(request,id):
    ranjan=studentsdata.objects.get(id=id)
    ranjan.delete()
    return redirect('fetching')