from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	title = models.CharField(max_length=100)

	class Meta:
		['user', 'title']