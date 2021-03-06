# Generated by Django 4.0.2 on 2022-02-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('subtitle', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, default='')),
                ('vidio_url', models.CharField(max_length=128)),
                ('price', models.FloatField(default=0)),
                ('image', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
