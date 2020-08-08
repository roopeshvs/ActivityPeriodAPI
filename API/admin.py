from django.contrib import admin

# Register your models here.
from API.models import UserModel, ActivityPeriodModel

admin.site.register(UserModel)
admin.site.register(ActivityPeriodModel)