# Generated by Django 4.0.4 on 2022-05-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_alter_album_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='released',
            field=models.CharField(max_length=60),
        ),
    ]