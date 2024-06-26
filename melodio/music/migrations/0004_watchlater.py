# Generated by Django 5.0.3 on 2024-04-07 05:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_genre_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchLater',
            fields=[
                ('listen_id', models.AutoField(primary_key=True, serialize=False)),
                ('songs_id', models.CharField(default='', max_length=10000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
