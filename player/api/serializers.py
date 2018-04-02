import json

from django.contrib.auth.models import User
from rest_framework import serializers

from player.models import Player


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')

    class Meta:
        model = Player
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'username',
            'dob',
        ]

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data.pop('user'))
        player_data = {
            'user': user,
            'dob': validated_data['dob'],
        }
        return Player.objects.create(**player_data)


class ChangePasswordSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        user = kwargs.get('user')
        if isinstance(user, User):
            user.set_password(self.validated_data.pop('password'))
            user.save()

    class Meta:
        model = User
        fields = [
            'password',
        ]

