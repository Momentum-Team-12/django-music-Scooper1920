# Generated by Django 4.0.4 on 2022-05-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0007_alter_album_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
