# Generated by Django 3.2.16 on 2023-01-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HFFRONTENDDJ', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finda',
            name='image',
            field=models.ImageField(upload_to='newimages'),
        ),
    ]