# Generated by Django 3.2.6 on 2021-10-24 02:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_remove_group_groupname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='group',
            new_name='groupies',
        ),
        migrations.RenameModel(
            old_name='WebName',
            new_name='wookname',
        ),
        migrations.RenameField(
            model_name='groupies',
            old_name='webName',
            new_name='pookname',
        ),
    ]
