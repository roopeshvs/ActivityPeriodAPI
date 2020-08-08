from rest_framework import serializers
from API.models import UserModel, ActivityPeriodModel

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriodModel
        fields = ['start_time', 'end_time']

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(read_only=True, many=True)
    class Meta:
        model = UserModel
        fields = ['id', 'real_name', 'tz', 'activity_periods']