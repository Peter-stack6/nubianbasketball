from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile, TutorialVideo, FAQ

class Register(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': False}
        }

    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = ['age', 'height', 'weight', 'physique', 'payment_status']

class TutorialSerializer(serializers.Serializer):
    class Meta:
        model = TutorialVideo
        fields = ['title', 'description', 'url']

class FAQParser(serializers.Serializer):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']