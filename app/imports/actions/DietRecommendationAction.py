from rest_framework import status

from app.models.activity import Activity
from app.models.allergie import Allergie
from app.models.diet_recommendation import DietRecommendation
from app.models.dietary_restriction import DietaryRestriction
from app.models.disease_type import DiseaseType
from app.models.gender import Gender
from app.models.member import Member
from app.models.preferred_cuisine import PreferredCuisine
from app.models.recommendation import Recommendation
from app.models.severity import Severity

from app.schemas.diet_recommendation import DietRecommendationScheme, ValidDietRecommendationScheme
from app.schemas.member import PartMemberScheme

from app.utils.logger import logger
from app.utils.types import AnyUser
from app.utils.validation import validate_fields_data

from logs.levels import LogLevel

from . import BaseAction

class DietRecommendationAction(BaseAction):

    def __init__(self, user: AnyUser):
        super().__init__(DietRecommendationScheme, user)

    def handle(self, data: list[DietRecommendationScheme]):
        fields = [
            {"name": "activity", "model": Activity, "is_list": False},
            {"name": "allergies", "model": Allergie, "is_list": True},
            {"name": "dietary_restrictions", "model": DietaryRestriction, "is_list": True},
            {"name": "disease_type", "model": DiseaseType, "is_list": False},
            {"name": "preferred_cuisine", "model": PreferredCuisine, "is_list": False},
            {"name": "recommendation", "model": Recommendation, "is_list": False},
            {"name": "severity", "model": Severity, "is_list": False},
        ]
        invalid_value = validate_fields_data(data, fields)
        if invalid_value:
            return logger.invalid_fields(invalid_value)

        valid_scheme, errors = self.tryGetMember(data)

        if len(errors) > 0:
            return logger.new(
                level = LogLevel.ERROR,
                message = "Some data are not valid, no member found",
                context = {
                    "count": len(errors),
                    "rows": errors
                },
                http_code = status.HTTP_400_BAD_REQUEST
            )

        for scheme in valid_scheme:

            activity = Activity.objects.get(value=self.upper(scheme.activity))
            allergies = Allergie.objects.filter(value__in=self.upper(scheme.allergies))
            dietary_restrictions = DietaryRestriction.objects.filter(value__in=self.upper(scheme.dietary_restrictions))
            disease_type = DiseaseType.objects.get(value=self.upper(scheme.disease_type))
            preferred_cuisine = PreferredCuisine.objects.get(value=self.upper(scheme.preferred_cuisine))
            recommendation = Recommendation.objects.get(value=self.upper(scheme.recommendation))
            severity = Severity.objects.get(value=self.upper(scheme.severity))

            diet_recommendation, _ = DietRecommendation.objects.get_or_create(
                adherence_to_diet_plan = scheme.adherence_to_diet_plan,
                blood_pressure = scheme.blood_pressure,
                cholesterol = scheme.cholesterol,
                daily_caloric_intake = scheme.daily_caloric_intake,
                dietary_nutrient_imbalance_score = scheme.dietary_nutrient_imbalance_score,
                glucose = scheme.glucose,
                weekly_exercise_hours = scheme.weekly_exercise_hours,

                activity=activity,
                disease_type=disease_type,
                member=scheme.member,
                preferred_cuisine=preferred_cuisine,
                recommendation=recommendation,
                severity=severity,
            )

            diet_recommendation.allergies.set(allergies)
            diet_recommendation.dietary_restrictions.set(dietary_restrictions)
            diet_recommendation.save()

        return self.success(len(valid_scheme))

    def tryGetMember(self, data: list[DietRecommendationScheme]) -> tuple[list[ValidDietRecommendationScheme], list]:
        valid_scheme: list[ValidDietRecommendationScheme] = []
        errors = []

        for scheme in data:

            member_scheme = PartMemberScheme(**scheme.model_dump())
            fields = [
                {"key": "gender", "model": Gender, "field": "value"}
            ]
            member_data = member_scheme.model_dump()
            member_data["client"] = self.user
            for field in fields:
                v = member_data[field["key"]]
                m = field["model"].objects.get(**{field["field"]: self.upper(v) if isinstance(v, str) else v})
                member_data[field["key"]] = m

            members = Member.objects.filter(**member_data)
            match len(members):
                case 0:
                    errors.append({"message": "Member DoNotExist", "context": scheme.model_dump()})
                case 1:
                    tmp = scheme.model_dump()
                    tmp["member"] = members[0]
                    valid_scheme.append(ValidDietRecommendationScheme(**tmp))
                case _:
                    errors.append({"message": "Member MultipleObjectsReturned", "context": scheme.model_dump()})

        return valid_scheme, errors
