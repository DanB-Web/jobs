from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ContactForm

class ContactView(CreateView):
    form_class = ContactForm
    template_name = "contact/contactForm.html"
    success_url = reverse_lazy('job-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # [TODO] - Add job details from params
        context['job'] = 'Test job'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)