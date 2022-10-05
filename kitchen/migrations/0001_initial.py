# Generated by Django 4.0.5 on 2022-08-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('height', models.FloatField(default=0)),
                ('width', models.FloatField(default=0)),
                ('length', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('price_worktop_profile', models.FloatField(default=0, null=True)),
                ('material', models.CharField(default='Material', max_length=50)),
                ('note', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='media/default-product.jpeg', null=True, upload_to='images/')),
                ('category', models.CharField(blank=True, choices=[('SI', 'Sink'), ('MX', 'Mixer')], max_length=2, null=True)),
            ],
        ),
    ]
