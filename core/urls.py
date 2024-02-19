from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from jobs.views import JobsDetail, JobsList

urlpatterns = [
    # Admin area
    path("admin/", admin.site.urls),
    # Tailwind hot reload
    path("__reload__/", include("django_browser_reload.urls")),
    # Admin WYSIWYG editor
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    # Site urls
    path("", JobsList.as_view(), name='job-list'),
    path("job/<uuid:pk>", JobsDetail.as_view(), name="job")


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin config
admin.site.index_title = "DevJobs Administration Area"

# if settings.DEBUG:
#     # Add static url
#     urlpatterns += static(settings.STATIC_URL)
#     # Add media url
#     urlpatterns += static(settings.MEDIA_URL)
#     # Add docs url
#     # urlpatterns += static(document_root=settings.MEDIA_ROOT)
