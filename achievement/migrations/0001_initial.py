# Generated by Django 2.1.5 on 2021-12-16 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('achv_no', models.IntegerField(primary_key=True, serialize=False)),
                ('achv_name', models.CharField(max_length=100)),
                ('achv_content', models.CharField(max_length=500)),
                ('achv_condition', models.CharField(max_length=100)),
                ('achv_image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AchievementPersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achv_no', models.IntegerField()),
                ('username', models.CharField(max_length=150)),
                ('get_date', models.DateField()),
            ],
        ),
    ]
