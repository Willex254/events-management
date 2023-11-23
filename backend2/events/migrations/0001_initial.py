# Generated by Django 4.2.7 on 2023-11-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('venue', models.CharField(max_length=255)),
                ('organizer', models.CharField(max_length=255)),
                ('banner', models.ImageField(blank=True, null=True, upload_to='event_banners/')),
            ],
        ),
    ]