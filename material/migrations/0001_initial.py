# Generated by Django 4.2.2 on 2023-07-21 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studyMaterial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('file', models.FileField(null=True, upload_to='static/upload/material')),
                ('link', models.URLField(null=True)),
                ('stat', models.IntegerField(default=0)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.mentor')),
            ],
        ),
    ]
