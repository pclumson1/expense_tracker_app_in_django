
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.urls import reverse

# Create your models here.
class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=72)
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2)
    photo = models.FileField(_("photo"), upload_to='media/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('expense_detail', args=[str(self.id)])

