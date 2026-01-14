from enum import Enum
from pydantic import BaseModel

class ClassEnum(str, Enum):
    ExerciceAction = 'ExerciceAction'

class ImportRequest(BaseModel):
    classname: ClassEnum
    data: list[object]
