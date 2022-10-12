from django.urls import path

from {{cookiecutter.slug}}.members import views

app_name = "members"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
