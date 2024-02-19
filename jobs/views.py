from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from .models import Job

class JobsList(ListView):
  template_name = "jobs/jobsList.html"
  model = Job
  context_object_name = 'jobs'
  paginate_by = 6

  def get_queryset(self):
    queryset = Job.objects.all().order_by('posted_at')
    return queryset
  
class JobsSearchResults(ListView):
  template_name = "jobs/jobsList.html"
  model = Job
  context_object_name = 'jobs'
  paginate_by = 3

  def get_queryset(self):
    # Add params etc here
    queryset = Job.objects.all().order_by('posted_at')
    return queryset

class JobsDetail(DetailView):
  template_name = "jobs/jobsDetail.html"
  model = Job
  context_object_name = 'job'

  def get_queryset(self):
    job_id = self.kwargs['pk']
    queryset = Job.objects.filter(uuid=job_id)
    return queryset