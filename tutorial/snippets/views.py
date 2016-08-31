from snippets.models import UserProfile
from snippets.serializers import UserProfileSerializer
from rest_framework import generics


class UserProfileList(generics.ListAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

class UserProfileView(generics.RetrieveAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

class UserProfileCreate(generics.CreateAPIView):
	serializer_class = UserProfileSerializer
