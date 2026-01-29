from pydantic import BaseModel

class ValidationErrorItem(BaseModel):
    fields: list[str]
    message: str
    input: str
    expected: str
