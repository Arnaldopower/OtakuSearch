from django.urls import path
from .views import SignUpView, LoginView, LogoutView, DeleteView

urlpatterns = [
    path("signup", SignUpView.as_view(), name="signup"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("delete", DeleteView.as_view(), name='delete'),
]
