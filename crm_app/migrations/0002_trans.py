# Generated by Django 4.2.1 on 2023-05-31 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('transcode', models.CharField(max_length=100)),
            ],
        ),
    ]
