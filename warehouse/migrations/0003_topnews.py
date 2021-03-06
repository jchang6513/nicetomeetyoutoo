# Generated by Django 2.1 on 2018-08-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse', '0002_delete_topnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=300)),
                ('photo', models.CharField(max_length=300)),
                ('headline', models.CharField(max_length=300)),
                ('body', models.CharField(max_length=300, unique=True)),
            ],
            options={
                'db_table': 'top_news',
            },
        ),
    ]
