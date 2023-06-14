from django.shortcuts import render

# Create your views here.
def list_projects(request):
    content = 'Hi Bassam'
    return render(request, 'list_projects.html', {'content':content})