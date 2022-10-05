# Generated by Django 4.0.5 on 2022-09-20 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0003_remove_kitchen_image5'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitchen',
            name='name',
        ),
        migrations.AddField(
            model_name='kitchen',
            name='name_en',
            field=models.CharField(default='Kitchen', max_length=255),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='name_ge',
            field=models.CharField(default='სამზარეულო', max_length=255),
        ),
    ]
