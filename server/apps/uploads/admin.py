from django.contrib import admin

# Register your models here.
from server.apps.uploads.models import FileUpload

admin.site.register(FileUpload)
