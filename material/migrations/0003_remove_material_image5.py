# Generated by Django 4.0.5 on 2022-08-31 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_rename_note_material_note_en_material_image2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='image5',
        ),
    ]
