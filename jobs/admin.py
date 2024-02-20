from django.contrib import admin
from .models import Company, Job

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
  readonly_fields = ("uuid",)
  list_display = ["company_name",]


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
  list_display = ["position", "company", "contract", "location", "posted_at"]
  # Flags the company FK relationship and optimzes query
  list_select_related = ["company"]
  list_filter = ("company", "contract", "location")
  # Note syntax to search for FK releationship
  search_fields = ("position", "company__company_name", "location")
  readonly_fields = ("uuid",)
  list_per_page = 6
  ordering = ('-posted_at',)
