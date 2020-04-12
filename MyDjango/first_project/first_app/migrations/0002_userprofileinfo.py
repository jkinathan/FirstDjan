# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(upload_to=b'profile_pics', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL,on_delete = models.CASCADE)),
                
            ],
        ),
    ]
