# Generated by Django 4.0.6 on 2022-07-31 20:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import first_app.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecord',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accessrecord',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.FileField(blank=True, null=True, upload_to=first_app.models.upload_location)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=False)),
                ('publish', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]