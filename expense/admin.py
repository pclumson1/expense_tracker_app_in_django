from django.contrib import admin

# Register your models here.

# Register your models here.
from django.db.models import Q
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _

# project related
from .models import Expense

admin.site.register(Expense)
