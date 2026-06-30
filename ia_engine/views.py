import torch

from django.http import HttpRequest

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from app.models.member import Member
from app.serializers.member import MemberSerializer

from core.utils.logger import logger
from core.utils.response import JsonResponse

from ia_engine.engine import IA
from ia_engine.database import test
from ia_engine.train import train

class IAViewSet(viewsets.ViewSet):

    def get_permissions(self):
        if self.action in ["recommendation"]:
            return [IsAuthenticated()]
        return [IsAdminUser()]

    def list(self, _: HttpRequest):
        return JsonResponse.success([
            "evaluate",
            "recommendation",
            "test",
            "train",
        ])

    @action(detail=False, methods=['get'])
    def recommendation(self, request: HttpRequest):
        ia = IA()
        logger.log.info("IA | 🚀 Démarrage du script de test de l'IA...")

        try:
            member: dict = MemberSerializer(Member.objects.get(user=request.user)).data
        except Member.DoesNotExist:
            logger.log.error(f"IA | Member for user={request.user.username} not found.")
            return JsonResponse.response({"message": "Your account has not be found."}, 404)

        # 2. Extraction et normalisation des données (Préparation pour l'IA)
        obj_str = member.get("objective", {}).get("value", "GAIN_WEIGHT")
        id_obj = 0.0 if obj_str == "GAIN_WEIGHT" else 1.0

        features = [
            id_obj,
            float(member.get("age", 20)) / ia.MAX_VALS["age"],
            float(member.get("bmi", 0)) / ia.MAX_VALS["bmi"],
            float(member.get("fat_percentage", 0)) / ia.MAX_VALS["fat"],
            float(member.get("workout_frequency", 0)) / ia.MAX_VALS["freq"]
        ]

        ia.engine.eval()

        # 4. Conversion en tenseur PyTorch et calcul de la prédiction
        input_tensor = torch.tensor([features], dtype=torch.float32)

        with torch.no_grad():
            predictions_brutes = ia.engine(input_tensor)
            # On récupère l'index de la classe qui a le score le plus élevé (0, 1 ou 2)
            id_status_predit = torch.argmax(predictions_brutes, dim=1).item()

        logger.log.info(f"IA | 📊 Classe prédite par l'IA (depuis MongoDB) : {id_status_predit}")

        # 5. Passage dans le moteur modulaire
        phrase_recommandation = ia.generer_recommandation_profile(id_status_predit, member)

        exercices = ia.recuperer_exercice_recommmande(id_status_predit, member)

        # 6. Affichage du résultat final
        logger.log.info("IA | 📝 RÉPONSE ENVOYÉE PAR L'IA :")
        logger.log.info(f"IA | {phrase_recommandation}")
        return JsonResponse.success({
            "message": phrase_recommandation,
            "exercices": exercices,
        })

    @action(detail=False, methods=['get'])
    def evaluate(self, _: HttpRequest):
        ia = IA()
        return JsonResponse.success(ia.evaluate())

    @action(detail=False, methods=['get'])
    def test(self, _: HttpRequest):
        return test()

    @action(detail=False, methods=['get'])
    def train(self, request: HttpRequest):
        return train(int(request.GET.get('count', '50000')))
