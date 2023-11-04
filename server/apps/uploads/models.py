import uuid

from django.db import models

from server.apps.account.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class FileUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to="uploads/")
    share_link = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    download_limit = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)],
    )
    expiration_date = models.DateTimeField()
