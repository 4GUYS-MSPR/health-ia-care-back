from django.core.management.base import BaseCommand, CommandError
from django.utils.module_loading import import_string

from app.models import Exercice, Member, Session

from core.models.factory import Factory
from core.utils.logger import logger
from core.utils.string import to_snake_case

from nutrition.models import DietRecommendation, Food

class Command(BaseCommand):
    help = "Model factory"

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--number',
            type=int,
            help='Number of factory to create per models',
            default=1
        )
        parser.add_argument('models', nargs='+', type=str, help="Models to seed with fake informations")

    def get_app_name(self, model: str) -> str:
        data = {
            DietRecommendation.__name__: 'nutrition',
            Exercice.__name__: 'app',
            Food.__name__: 'nutrition',
            Member.__name__: 'app',
            Session.__name__: 'app',
        }
        return data[model]

    def handle(self, *args, **options):
        n = options.get('number')
        models = options.get('models')
        avalaible = [
            DietRecommendation.__name__,
            Exercice.__name__,
            Food.__name__,
            Member.__name__,
            Session.__name__,
        ]
        try:
            count = 0
            for model in models:    
                if model not in avalaible:
                    logger.log.warning(f"Model {model} not valid !")
                    continue
                app = self.get_app_name(model)
                filename = to_snake_case(model)
                path = f"{app}.models.factory.{filename}"
                try:
                    cls = import_string(path)
                except ImportError as e:
                    raise ValueError(f"Invalid classname file: {str(e)}") from e
                factory_class: Factory = cls()
                factory_class.handle(n)
                count+=n
        except CommandError as e:
            logger.log.exception(e)
