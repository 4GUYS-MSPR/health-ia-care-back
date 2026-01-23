from enum import Enum
from pydantic import BaseModel

class ActionEnum(str, Enum):
    ExerciceAction = 'ExerciceAction'
    FoodAction= 'FoodAction'
    MemberAction = 'MemberAction'
    SessionAction= 'SessionAction'

class ImportRequest(BaseModel):
    classname: ActionEnum
    data: list[object]

class PartialImportRequest(BaseModel):
    classname: ActionEnum
