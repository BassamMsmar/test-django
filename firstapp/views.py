from django.shortcuts import render
from simple_history.models import HistoricalRecords


from .models import Student
from .forms import StudentForm

# Create your views here.
def students(request):
    students = Student.objects.all()
    # historical_records = HistoricalRecords.objects.all() 
    return render(request, 'list_student.html', {
        'students':students,
        # 'historical_records':historical_records
        })


def add_student(request):
    form = StudentForm()
    return render(request, 'add_student.html',{'form':form})


def detail_student(request, pk):
    student = Student.objects.get(pk=pk)


    return render(request, 'detail_student.html', {
        'student':student
    })
  



def views_student(request):
    phone = request.POST['phone']
    student= Student.objects.get(phone=int(phone))
    form = StudentForm()
    return render(request, 'list.html', {
        'student':student,
        'form':form,
        })
    
