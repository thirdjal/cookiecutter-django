from django.urls import path

from {{cookiecutter.slug}}.members.views import SignupView

app_name = "members"
urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
]
