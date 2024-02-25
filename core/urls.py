from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Admin area
    path("admin/", admin.site.urls),
    # Tailwind hot reload
    path("__reload__/", include("django_browser_reload.urls")),
    # Admin WYSIWYG editor
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    # Job app urls
    path("", include('jobs.urls')),
    # Contact app urls
    path("", include('contact.urls'))
]


# Admin config
admin.site.index_title = "DevJobs Administration Area"

if settings.DEBUG:
# Add static urls
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Add media urls
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 # Add debug toolbar
 urlpatterns += path("__debug__/", include("debug_toolbar.urls")),
