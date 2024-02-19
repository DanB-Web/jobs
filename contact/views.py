from django.views.generic import FormView
from .forms import ContactForm

class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact/contactForm.html"