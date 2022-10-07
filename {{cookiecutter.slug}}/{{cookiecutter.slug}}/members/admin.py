from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MemberChangeForm, MemberCreationForm
from .models import Member


@admin.register(Member)
class MemberAdmin(UserAdmin):
    add_form = MemberCreationForm
    form = MemberChangeForm
