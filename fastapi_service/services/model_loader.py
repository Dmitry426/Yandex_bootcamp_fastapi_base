import logging
import os
from abc import ABC
from typing import Any

import boto3

from fastapi_service.settings.settings import settings, Settings

LOCAL_MODELS_PATH = os.path.dirname(settings.project.base_dir) + settings.project.models_path

logger = logging.getLogger(__name__)

s3 = boto3.client('s3')


class AbstractModelGetter(ABC):

    def get_model(self, conf: Settings) -> Any:
        """Get model from S3 if possible
        """

        raise NotImplemented


class ModelLoader(AbstractModelGetter):
    def get_model(self, conf: Settings) -> bytes:
        response = s3.get_object(Bucket=conf.s3.bucket_name, Key=conf.s3.model_key)
        model_bytes = response['Body'].read()
        return model_bytes


def get_torch_models() -> bytes:
    return ModelLoader().get_model(settings)
