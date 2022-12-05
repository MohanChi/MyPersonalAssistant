# Generated by Django 3.2.16 on 2022-12-04 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssistantApp', '0002_alter_task_model_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]