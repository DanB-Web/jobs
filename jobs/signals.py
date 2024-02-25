from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Job
from bs4 import BeautifulSoup

@receiver(pre_save, sender=Job)
def strip_span_tags(sender, instance, **kwargs):
    raw_description = BeautifulSoup(instance.description)
    raw_requirements = BeautifulSoup(instance.requirements)
    raw_role = BeautifulSoup(instance.role)

    for span_tag in raw_description.find_all('span'):
      span_tag.replace_with_children()

    for span_tag in raw_requirements.find_all('span'):
      span_tag.replace_with_children()

    for span_tag in raw_role.find_all('span'):
      span_tag.replace_with_children()

    instance.description = str(raw_description)
    instance.requirements = str(raw_requirements)
    instance.role = str(raw_role)