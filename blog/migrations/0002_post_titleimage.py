# Generated by Django 4.2.7 on 2024-05-31 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titleImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
