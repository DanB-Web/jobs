from django.db import models
from jobs.models import Job 

class Contact(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  message = models.CharField(max_length=1000)
  job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job")
  job_uuid = models.CharField(max_length=100)
  contact_received = models.DateTimeField(auto_now_add=True)
  replied = models.BooleanField(default=False)

  def __str__(self):
    return f'{self.name} re {self.job}'