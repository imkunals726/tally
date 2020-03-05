from django.db import models
from django_extensions.db.models import TimeStampedModel
# Create your models here.
class UploadedFile( TimeStampedModel ):
	file_name = models.TextField(default="")
	file_url = models.TextField(default="" )