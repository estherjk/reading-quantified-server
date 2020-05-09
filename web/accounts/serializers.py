from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        # Show only a subset of the fields
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        )

        read_only_fields = (
            'username',
        )