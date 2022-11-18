from django.db import models
from uuid import uuid4
# Create your models here.

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    release_date = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publish_company = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    