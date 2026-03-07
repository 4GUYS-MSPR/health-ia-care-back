from rest_framework import serializers

class EnumItemSerializer(serializers.Serializer): # pylint: disable=abstract-method
    id = serializers.IntegerField()
    value = serializers.CharField()
    create_at = serializers.DateTimeField(allow_null=True)
