from django.shortcuts import render

def index(request):
  context = {}
  print('index')
  return render(request, "jobs/jobsList.html", context)
