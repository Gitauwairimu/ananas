# Generated by Django 4.2.11 on 2024-05-08 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pesa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='transfered_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='funds_transferer', to=settings.AUTH_USER_MODEL),
        ),
    ]
