import uuid

from functools import partial
from django.db import models
from django.conf import settings


def get_pk_format():
    if settings.EAV2_PRIMARY_KEY_FIELD == "django.db.models.UUIDField":
        PrimaryField = partial(
            models.UUIDField, primary_key=True, editable=False, default=uuid.uuid4
        )
    elif settings.EAV2_PRIMARY_KEY_FIELD == "django.db.models.CharField":
        PrimaryField = partial(
            models.CharField, primary_key=True, editable=False, max_length=40
        )
    else:
        PrimaryField = partial(models.BigAutoField, primary_key=True, editable=False)
    return PrimaryField()