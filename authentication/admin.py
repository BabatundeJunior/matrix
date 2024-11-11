from django.contrib import admin
from django.contrib.auth.models import User

from .models import UserProfile

# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'  # Ensure this is set to 'user' to link it correctly

class UserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.register(UserProfile)
