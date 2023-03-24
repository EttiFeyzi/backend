# Generated by Django 4.1.7 on 2023-03-24 16:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, max_length=128, null=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(default=uuid.uuid1, max_length=30, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_client', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]