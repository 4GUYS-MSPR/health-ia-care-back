from django.apps import AppConfig

class SocialNetworkConfig(AppConfig):
    name = 'social_network'

    def ready(self):
        import social_network.signals # pylint: disable=unused-import
