from django.db import models

class Contact(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  message = models.CharField(max_length=1000)
  contact_received = models.DateTimeField(auto_now_add=True)
  replied = models.BooleanField(default=False)