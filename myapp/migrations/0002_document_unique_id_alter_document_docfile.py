# Generated by Django 4.1.4 on 2023-04-28 18:58

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='unique_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=myapp.models.content_file_name),
        ),
    ]