from django.urls import path
from contact.views import ContactView

urlpatterns = [
    path("contact/<uuid:pk>", ContactView.as_view(), name='contact'),
]