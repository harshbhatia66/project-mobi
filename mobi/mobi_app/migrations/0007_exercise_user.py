# Generated by Django 4.2.8 on 2024-01-14 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mobi_app', '0006_alter_set_notes_alter_set_reps_alter_set_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]