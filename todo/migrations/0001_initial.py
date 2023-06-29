# Generated by Django 4.2.2 on 2023-06-29 02:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('posted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
