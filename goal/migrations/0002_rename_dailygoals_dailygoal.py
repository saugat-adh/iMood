# Generated by Django 3.2.2 on 2022-02-15 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DailyGoals',
            new_name='DailyGoal',
        ),
    ]
