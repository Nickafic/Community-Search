# Generated by Django 3.2.6 on 2021-10-15 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(max_length=100)),
                ('webname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.webname')),
            ],
        ),
    ]
