# Generated by Django 3.1 on 2020-08-08 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.CharField(default='W012A3CDE', max_length=9, primary_key=True, serialize=False, unique=True)),
                ('real_name', models.CharField(max_length=50)),
                ('tz', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriodModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='API.usermodel')),
            ],
        ),
    ]
