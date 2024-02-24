from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm
from jobs.models import Job 

class ContactView(CreateView):
    form_class = ContactForm
    template_name = "contact/contactForm.html"
    success_url = reverse_lazy('job-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_id = self.kwargs.get('pk', None)
        job = Job.objects.filter(uuid=job_id).first()
        context['job'] = job
        return context

    def form_valid(self, form):
        job_id = self.request.POST.get('job_uuid', None)
        job = Job.objects.filter(uuid=job_id).first()
        form.save(commit=False)
        form.instance.job = job
        form.save()
        messages.success(self.request, 'Thank you for contacting us')
        return super().form_valid(form)