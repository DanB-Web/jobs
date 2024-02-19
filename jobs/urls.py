from django.urls import path
from jobs.views import JobsDetail, JobsList, JobsSearchResults

urlpatterns = [
    path("", JobsList.as_view(), name='job-list'),
    path("jobs/<uuid:pk>", JobsDetail.as_view(), name="job"),
    path("search", JobsSearchResults.as_view(), name="search"),
]