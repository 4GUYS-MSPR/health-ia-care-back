from typing import List
from urllib.parse import urlparse

from pydantic import BaseModel, field_validator

class ExerciceScheme(BaseModel):
    imageUrl: str

    bodyParts: List[str]
    exerciseType: str
    equipments: List[str]
    secondaryMuscles: List[str]
    targetMuscles: List[str]

    @field_validator("imageUrl")
    @classmethod
    def check_url(cls, v: str):
        result = urlparse(v)
        if not (result.scheme and result.netloc):
            raise ValueError(f"{v} is not a valid URL")
        return v

    @field_validator('equipments', 'bodyParts', 'targetMuscles', 'secondaryMuscles', mode='before')
    @classmethod
    def split_comma_string(cls, v):
        if isinstance(v, list):
            return v
        if isinstance(v, str):
            return [item.strip() for item in v.split(';') if item.strip()]
        return v
