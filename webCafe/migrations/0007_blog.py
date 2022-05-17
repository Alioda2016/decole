# Generated by Django 4.0.4 on 2022-05-10 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webCafe', '0006_rename_subject_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]
