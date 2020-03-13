# Generated by Django 3.0.4 on 2020-03-13 04:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_question_completed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='completed_by',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
