# Generated by Django 2.2.3 on 2019-07-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0007_story_city_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='slug',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]