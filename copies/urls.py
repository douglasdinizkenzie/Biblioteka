from django.urls import path

from .views import CopiesView, BookLoanView

urlpatterns = [
    path("books/copies/<int:pk>/", CopiesView.as_view()),
    path("copies/loan/<int:pk>/", BookLoanView.as_view())
    ]
