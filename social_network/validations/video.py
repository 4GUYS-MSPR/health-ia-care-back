import mimetypes

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile

def validate_video(file: UploadedFile):
    mime, _ = mimetypes.guess_type(str(file.name))

    if not mime or not mime.startswith("video"):
        raise ValidationError("File should be a video")
