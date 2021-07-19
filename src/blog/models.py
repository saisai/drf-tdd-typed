from django.db import models
from django.conf import settings
from core.models import BaseModel, User, generate_uuid_for_file_with_dir


def generate_uuid_for_author_avatar(_, original_file_name: str):
    return generate_uuid_for_file_with_dir(original_file_name, settings.UPLOAD_TO_AUTHOR_AVATAR)


class Author(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=generate_uuid_for_author_avatar, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self) -> str:
        return self.user.username
