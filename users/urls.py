from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from copies.views import BookLoanView, BookLoanDetailView

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/<int:user_id>/loans/<int:loan_id>/", BookLoanView.as_view()),
    path("users/<int:user_id>/loans/", BookLoanDetailView.as_view()) 
]
