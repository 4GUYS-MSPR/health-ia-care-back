from django.forms import ModelForm

from social_network.models import Publication

class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ["type", "image", "video"]
