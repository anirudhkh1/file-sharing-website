# Generated by Django 4.2.7 on 2023-11-04 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='expiration_days',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='expiration_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]