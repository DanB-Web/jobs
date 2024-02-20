from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  readonly_fields = ("name", "job", "email", "message", "contact_received")
  list_display = ["name", "job", "email", "contact_received", "replied"]
  exclude = ["job_uuid"]
