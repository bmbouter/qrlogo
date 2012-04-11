from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to="images/%Y/%m/%d")