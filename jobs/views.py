from urllib.parse import urlparse
from django.db.models import Q
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Job

class JobsList(ListView):
  template_name = "jobs/jobsIndex.html"
  model = Job
  context_object_name = 'jobs'
  paginate_by = 6

  def get_queryset(self):
    queryset = Job.objects.all().order_by('-posted_at')

    # Format posted date
    for job in queryset:
      delta = timezone.now().date() - job.posted_at
      job.delta_days = delta.days

    return queryset
  
  

class JobsSearchResults(ListView):
  template_name = "jobs/jobsSearchResults.html"
  model = Job
  context_object_name = 'jobs'

  '''
  Note that you have to reassign to the queryset after each filter
  '''
  def get_queryset(self):
    job = self.request.GET.get("job")
    location = self.request.GET.get("location")
    contract = self.request.GET.get("contract")
    queryset = Job.objects.all()
    if job:
      queryset = queryset.filter(
            Q(position__icontains=job) | 
            Q(company__company_name__icontains=job) 
        )
    if location:
      queryset = queryset.filter(location__icontains=location)
    if contract == 'on':
      queryset = queryset.filter(contract='full_time')

    # OPTION 1 - format posted date on queryset itself
    for job in queryset:
      delta = timezone.now().date() - job.posted_at
      job.delta_days = delta.days
    
    return queryset
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['job'] = self.request.GET.get("job")
      context['location'] = self.request.GET.get("location")
      context['contract'] = self.request.GET.get("contract")
  
      return context


class JobsDetail(DetailView):
  template_name = "jobs/jobDetail.html"
  model = Job
  context_object_name = 'job'

  def get_queryset(self):
    job_id = self.kwargs['pk']
    queryset = Job.objects.filter(uuid=job_id)
    return queryset
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)

      queryset = self.get_queryset()[0]

      # OPTION 2 - Format posted day and add to context
      queryset.job.delta_days = timezone.now().date() - queryset.posted_at
      delta = timezone.now().date() - queryset.posted_at
      context['delta_days'] = delta.days

      # Extract domain from the URL and add it to the context
      context['company_domain'] = urlparse(queryset.company.website).netloc

      # Enable footer for this view
      context['footer'] = True

      return context