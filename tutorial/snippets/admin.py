from django.contrib import admin
from snippets.models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.
# class UserProfileAdmin(admin.ModelAdmin):
# 	pass
#
# admin.site.register(UserProfile, UserProfileAdmin)

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	verbose_name_plural = "User Profiles"


class UserAdmin(UserAdmin):
	inlines = (UserProfileInline, )
	list_display = ['username', 'id', 'first_name', 'last_name']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)