from django.test import SimpleTestCase
from pydantic import ValidationError
from core.imports.request import ImportRequest
from app.schemas.member import MemberScheme

class TestImportValidation(SimpleTestCase):

    def test_pydantic_should_fail_on_invalid_classname(self):
        payload = {
            "classname": "ActionNone", 
            "data": [{"some": "data"}]
        }
        with self.assertRaises(ValidationError):
            ImportRequest(classname=payload["classname"], data=payload["data"])

    def test_pydantic_should_fail_if_data_is_not_list(self):
        payload = {
            "classname": "MemberAction",
            "data": "Not a list"
        }
        with self.assertRaises(ValidationError):
            ImportRequest(classname=payload["classname"], data=payload["data"])

    def test_memeber_scheme_should_verify_datas(self):
        data = {
            "age" : 25,
            "bmi" : 22.5,
            "fat_percentage" : 15.0,
            "height" : 185.0,
            "weight" : 75.0,
            "workout_frequency" : 3,
            "level" : 1
        }

        member = MemberScheme(**data)

        self.assertEqual(member.height, 1.85)
        self.assertIsNot(member.age, float)
