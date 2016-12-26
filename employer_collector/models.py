from django.db import models


class Employers(models.Model):
    employer = models.CharField(max_length=512, unique=True)
    email = models.EmailField(max_length=512, unique=True)
    site = models.CharField(max_length=512, unique=True)
    is_send = models.BooleanField(default=False)
    when_send = models.DateField(auto_now=True)
    response = models.CharField(max_length=512, default='No response')
