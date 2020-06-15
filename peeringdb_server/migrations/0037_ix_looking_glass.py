# Generated by Django 2.2.12 on 2020-05-14 06:44

from django.db import migrations
import django_peeringdb.models.abstract


class Migration(migrations.Migration):

    dependencies = [
        ('peeringdb_server', '0036_ixlanprefix_in_dfz'),
    ]

    operations = [
        migrations.AddField(
            model_name='internetexchange',
            name='looking_glass',
            field=django_peeringdb.models.abstract.LG_URLField(blank=True, max_length=255),
        ),
    ]