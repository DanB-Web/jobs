from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  readonly_fields = ("name", "email", "message", "contact_received")
  list_display = ["name", "email", "contact_received", "replied"]
