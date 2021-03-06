# Generated by Django 2.2 on 2021-02-16 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_user_skill_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='skill_level',
            field=models.CharField(default='Beginner', max_length=255),
        ),
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default="default='default.jpg", upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('likes', models.ManyToManyField(related_name='liked_images', to='app1.User')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app1.User')),
            ],
        ),
    ]
