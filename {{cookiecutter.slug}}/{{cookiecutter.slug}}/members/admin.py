from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from {{cookiecutter.slug}}.members.forms import MemberChangeForm, MemberCreationForm
from {{cookiecutter.slug}}.members.models import Member


@admin.register(Member)
class MemberAdmin(UserAdmin):
    add_form = MemberCreationForm
    form = MemberChangeForm
