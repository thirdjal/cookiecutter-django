from django.contrib.auth import views as auth_views

from {{cookiecutter.slug}}.members.forms import MemberAuthenticationForm


class LoginView(auth_views.LoginView):
    form_class = MemberAuthenticationForm
    template_name = "members/login.html"


class LogoutView(auth_views.LogoutView):
    pass
