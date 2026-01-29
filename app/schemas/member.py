from pydantic import BaseModel, field_validator, NonNegativeFloat, NonNegativeInt

class MemberScheme(BaseModel):
    age: NonNegativeInt
    bmi: NonNegativeFloat
    fat_percentage: NonNegativeFloat
    height: NonNegativeFloat
    weight: NonNegativeFloat
    workout_frequency: NonNegativeInt

    objectives: list = []

    gender: str = "NOT SPECIFIED"
    level: int
    subscription: str = "FREE"

    @field_validator("gender")
    @classmethod
    def check_gender(cls, v: str):
        return v if v != "" else "NOT SPECIFIED"

    @field_validator("height")
    @classmethod
    def normalize_height(cls, v: float) -> float:
        if v > 10:
            v = v / 100
        if not 0.5 <= v <= 2.5:
            raise ValueError("height must be between 0.5m and 2.5m")
        return round(v, 2)

class PartMemberScheme(BaseModel):
    age: NonNegativeInt
    height: NonNegativeFloat
    weight: NonNegativeFloat

    gender: str = "NOT SPECIFIED"

    @field_validator("height")
    @classmethod
    def normalize_height(cls, v: float) -> float:
        if v > 10:
            v = v / 100
        if not 0.5 <= v <= 2.5:
            raise ValueError("height must be between 0.5m and 2.5m")
        return round(v, 2)
