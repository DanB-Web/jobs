import uuid
from django.db import models
from django.core.validators import RegexValidator
from django_ckeditor_5.fields import CKEditor5Field

# note in template use get_FOO_display
# i.e {{ job.get_contract_display }}
CONTRACT_TYPES = [
  ('full_time', 'Full Time'),
  ('part_time', 'Part Time'),
  ('freelance', 'Freelance'),
]

class Company(models.Model):

  class Meta:
    verbose_name_plural = "companies"

  uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
  company_name = models.CharField(max_length=255)
  logo = models.FileField(upload_to='logos/')
  company_color = models.CharField(
        max_length=7,
        validators=[
            RegexValidator(
                regex='^#[0-9A-Fa-f]{6}$',
                message='Hex value must be in the format #XXXXXX',
                code='invalid_hex_value'
            )
        ]
    )
  website = models.URLField(max_length=255)

  def __str__(self):
    return self.company_name

class Job(models.Model):
  uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
  position = models.CharField(max_length=255, blank=False)
  posted_at = models.DateField()
  contract = models.CharField(max_length=255, choices=CONTRACT_TYPES, verbose_name="Contract type",default="full_time")
  location = models.CharField(max_length=255, verbose_name="Job location", blank=False)
  company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
  apply = models.URLField(max_length=255, verbose_name="Application URL", blank=False)
  description = CKEditor5Field('Job description', config_name='extends', blank=False)
  requirements = CKEditor5Field('Job requirements', config_name='extends', blank=False)
  role = CKEditor5Field('Role details', config_name='extends', blank=False)

  def __str__(self):
    return f'{self.position} at {self.company}'
  
  @property
  def job(self):
    return f'{self.position} at {self.company}'

