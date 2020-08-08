release: python manage.py migrate
release: python manage.py populate_users --path users.yaml
release: python manage.py populate_activity_periods --path activity_periods.yaml
web: python manage.py runserver 0.0.0.0:$PORT