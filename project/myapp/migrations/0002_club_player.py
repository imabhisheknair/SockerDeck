# Generated by Django 3.1.2 on 2020-10-27 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='club_player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_id', models.IntegerField()),
                ('player_id', models.IntegerField()),
            ],
        ),
    ]
