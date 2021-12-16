# Generated by Django 2.1.5 on 2021-12-16 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_no', models.IntegerField(primary_key=True, serialize=False)),
                ('quiz_title', models.CharField(max_length=30)),
                ('quiz_content', models.CharField(max_length=1000)),
                ('hint1', models.CharField(max_length=1000)),
                ('hint2', models.CharField(max_length=1000)),
                ('hint3', models.CharField(max_length=1000)),
                ('hint4', models.CharField(max_length=1000)),
                ('hint5', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1000)),
                ('quiz_summary', models.CharField(max_length=500)),
                ('quiz_image', models.CharField(max_length=200)),
            ],
        ),
    ]