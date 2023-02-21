from rest_framework import serializers
from .models import Thrive


class ThriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thrive
        fields = "__all__"
