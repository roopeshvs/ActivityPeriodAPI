import yaml
from django.core.management.base import BaseCommand
from API.models import UserModel

class Command(BaseCommand):
    help = 'Populate User Table From yaml'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        with open(options['path'], 'r') as stream:
            activities = yaml.safe_load(stream)
            for activity in activities:
                user_activity, _ = UserModel.objects.get_or_create(id=activity['id'])
                user_activity.real_name = activity['real_name']
                user_activity.tz = activity['tz']
                user_activity.save()

        self.stdout.write(self.style.SUCCESS('Successfully Populated Users!'))