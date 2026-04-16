import os
import uuid

def get_image_path(_, filename):
    ext = os.path.splitext(filename)[1]
    return f"publication/images/{uuid.uuid4()}{ext}"

def get_video_path(_, filename):
    ext = os.path.splitext(filename)[1]
    return f"publication/videos/{uuid.uuid4()}{ext}"

def get_avatar_path(_, filename):
    ext = os.path.splitext(filename)[1]
    return f"users/{uuid.uuid4()}{ext}"
