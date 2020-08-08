from django.db import models
from django.conf import settings

# User Model
class UserModel(models.Model):
    id = models.CharField(max_length=9, primary_key=True, unique=True, default='W012A3CDE') #Default set to counter a bug in Heroku Deployment
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=50)

# Activity Period Model
class ActivityPeriodModel(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='activity_periods')
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)