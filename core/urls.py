from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from jobs.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    # Tailwind hot reload
    path("__reload__/", include("django_browser_reload.urls")),
    # Admin WYSIWYG editor
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path("", index, name='jobs-list')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin config
admin.site.site_title = "DevJobs"
admin.site.site_header = "DevJobs"
admin.site.index_title = "DevJobs Administration"

# if settings.DEBUG:
#     # Add static url
#     urlpatterns += static(settings.STATIC_URL)
#     # Add media url
#     urlpatterns += static(settings.MEDIA_URL)
#     # Add docs url
#     # urlpatterns += static(document_root=settings.MEDIA_ROOT)
