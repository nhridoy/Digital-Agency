# Generated by Django 4.0 on 2021-12-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_reviewmodel_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customers', models.IntegerField()),
                ('presets', models.IntegerField()),
                ('responses', models.IntegerField()),
            ],
        ),
    ]