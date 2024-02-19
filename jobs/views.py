from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Job

class JobsList(ListView):
  template_name = "jobs/jobsIndex.html"
  model = Job
  context_object_name = 'jobs'
  paginate_by = 6

  def get_queryset(self):
    queryset = Job.objects.all().order_by('posted_at')
    return queryset
  

class JobsSearchResults(ListView):
  template_name = "jobs/jobsSearchResults.html"
  model = Job
  context_object_name = 'jobs'

  def get_queryset(self):
    query = self.request.GET.get("q")
    queryset = Job.objects.filter(
            Q(description__icontains=query) | Q(location__icontains=query) | Q(company__company_name__icontains=query)
        )
    return queryset


class JobsDetail(DetailView):
  template_name = "jobs/jobDetail.html"
  model = Job
  context_object_name = 'job'

  def get_queryset(self):
    job_id = self.kwargs['pk']
    queryset = Job.objects.filter(uuid=job_id)
    return queryset