import yaml
from django.core.management.base import BaseCommand
from API.models import ActivityPeriodModel, UserModel

class Command(BaseCommand):
    help = 'Populate Activity Table From yaml'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        with open(options['path'], 'r') as stream:
            activities = yaml.safe_load(stream)
            for activity in activities:
                foreign_key = UserModel.objects.get(activity_periods=activity['user_id'])
                user_activity, _ = ActivityPeriodModel.objects.get_or_create(user_id=foreign_key, start_time = activity['start_time'], end_time = activity['end_time'])
                user_activity.save()

        self.stdout.write(self.style.SUCCESS('Successfully Populated Activity Periods!'))