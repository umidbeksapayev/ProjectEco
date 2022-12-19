from rest_framework import serializers

from eco.models import EcoPost


class EcoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcoPost
        fields = ('id', 'title', 'body', 'created_time', 'image', 'author')
