# Generated by Django 4.2.8 on 2024-02-09 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobi_app', '0011_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='equipment_type',
            field=models.CharField(blank=True, help_text="Type of equipment used, e.g., 'Dumbbell', 'Machine'.", max_length=255),
        ),
        migrations.AddField(
            model_name='exercise',
            name='function',
            field=models.CharField(blank=True, help_text="Functional focus of the exercise, e.g., 'Chest', 'Legs'.", max_length=255),
        ),
        migrations.AddField(
            model_name='exercise',
            name='gif',
            field=models.FileField(blank=True, null=True, upload_to='exercise_gifs/'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='history',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='exercise_images/'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='instructions',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='workoutsession',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='type',
            field=models.CharField(help_text='Type of exercise, e.g., cardio, strength.', max_length=255),
        ),
    ]