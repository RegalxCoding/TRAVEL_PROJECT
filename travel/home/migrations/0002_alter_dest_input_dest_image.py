# Generated by Django 3.2.12 on 2024-12-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dest_input',
            name='dest_image',
            field=models.ImageField(upload_to='static'),
        ),
    ]