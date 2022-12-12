# Generated by Django 4.1.4 on 2022-12-12 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormProyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(max_length=400)),
                ('titulo_proyecto', models.CharField(max_length=200)),
                ('description_proyecto', models.TextField()),
                ('tags', models.CharField(max_length=100)),
                ('url_github', models.URLField(max_length=400)),
            ],
        ),
    ]
