from __future__ import absolute_import
from django.conf import settings

if not settings.DJANGO_1_10:
    from . import monkeypatch  # noqa

default_app_config = 'kuma.core.apps.CoreConfig'
