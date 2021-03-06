# Generated by Django 3.0 on 2022-01-05 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPropertyManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(default=None, max_length=100)),
                ('Link', models.CharField(default=None, max_length=500)),
                ('Image', models.ImageField(default=None, upload_to='static/Images')),
            ],
            options={
                'db_table': 'Digital Property',
            },
        ),
    ]
