from django.shortcuts import render
from .models import Student
from .forms import StudentForm

# Create your views here.
def students(request):
    students = Student.objects.all()
    return render(request, 'list_student.html', {'students':students})


def add_student(request):
    form = StudentForm()
    return render(request, 'add_student.html',{'form':form})



def views_student(request):
    phone = request.POST['phone']
    student= Student.objects.get(phone=int(phone))
    form = StudentForm()
    return render(request, 'list.html', {
        'student':student,
        'form':form,
        })
    
