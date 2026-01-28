from datetime import time
from typing import List

from pydantic import field_validator, NonNegativeFloat, NonNegativeInt

from .member import MemberScheme

class SessionScheme(MemberScheme):
    avg_bpm: NonNegativeInt
    calories_burned: NonNegativeFloat
    duration: time
    max_bpm: NonNegativeInt
    resting_bpm: NonNegativeInt
    water_intake: NonNegativeFloat
    exercices: List[NonNegativeInt] = []

    @field_validator("duration", mode="before")
    @classmethod
    def convert_duration(cls, v):
        if isinstance(v, time):
            return v

        if isinstance(v, str):
            v = v.strip()
            if v == "":
                raise ValueError("Duration is empty")
            try:
                v = float(v)
            except ValueError as exc:
                raise ValueError("Invalid duration format") from exc

        if isinstance(v, (float, int)):
            total_seconds = int(v * 3600)
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return time(hour=hours, minute=minutes, second=seconds)

        raise ValueError("Invalid duration format")
