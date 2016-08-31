from rest_framework import serializers
from snippets.models import UserProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = UserProfile
		fields = ('title', 'user')

	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user = User.objects.create(**user_data)

		return UserProfile.objects.create(user=user, **validated_data)
