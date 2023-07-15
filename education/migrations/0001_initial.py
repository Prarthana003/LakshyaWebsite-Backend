# Generated by Django 4.2.2 on 2023-07-15 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='abrodEdu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='applied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.candidate')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.abrodedu')),
            ],
            options={
                'unique_together': {('cadidate', 'post')},
            },
        ),
    ]
