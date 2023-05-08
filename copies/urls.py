from django.urls import path

from .views import CopiesView

urlpatterns = [
    path("books/copies/<int:pk>/", CopiesView.as_view())
    ]
