# Generated by Django 4.0.4 on 2022-06-01 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('innotter', '0005_rename_is_liked_post_liked_by'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='page',
            managers=[
                ('active_pages', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='follow_requests',
            field=models.ManyToManyField(blank=True, null=True, related_name='requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='page',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='follows', to=settings.AUTH_USER_MODEL),
        ),
    ]