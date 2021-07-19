import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


def generate_uuid_for_file_with_dir(original_file_name, upload_dir):
    extension = original_file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{extension}'
    return os.path.join(upload_dir, file_name)


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    pass
