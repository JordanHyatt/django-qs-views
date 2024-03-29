# Generated by Django 4.0.6 on 2024-02-26 16:16

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import qs_views.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='QsView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_name', models.CharField(max_length=255, unique=True)),
                ('db_alias', models.CharField(default='default', max_length=255)),
                ('get_qs_method_name', models.CharField(max_length=255)),
                ('fields', models.JSONField(blank=True, null=True)),
                ('ufields', models.JSONField(blank=True, null=True, verbose_name='Unique Fields')),
                ('materialized', models.BooleanField(default=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('dtg_last_refresh', models.DateTimeField(blank=True, null=True)),
                ('dtg_view_created', models.DateTimeField(blank=True, null=True)),
                ('db_owner', models.CharField(default=qs_views.models.get_db_owner_default, max_length=50)),
                ('db_read_only_users', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=None)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('owners', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-dtg_last_refresh', '-dtg_view_created'),
            },
        ),
    ]
