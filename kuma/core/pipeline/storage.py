from __future__ import absolute_import
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from pipeline.storage import PipelineMixin


class ManifestPipelineStorage(PipelineMixin, ManifestStaticFilesStorage):
    pass
