# Generated by Django 2.2 on 2021-02-15 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='image',
            name='posted_by',
        ),
        migrations.DeleteModel(
            name='Catagory',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
