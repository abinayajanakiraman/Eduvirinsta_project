# Generated by Django 3.1.3 on 2020-11-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=50)),
                ('job_Class', models.IntegerField(default=1)),
                ('regno', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='School_Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('Regno', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('stand', models.IntegerField()),
                ('Regno', models.IntegerField(unique=True)),
                ('subj', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='stand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('stand', models.IntegerField()),
                ('tamil', models.IntegerField(default=0)),
                ('science', models.IntegerField(default=0)),
                ('Maths', models.IntegerField(default=0)),
                ('Social', models.IntegerField(default=0)),
                ('English', models.IntegerField(default=0)),
                ('Regno', models.IntegerField(unique=True)),
            ],
        ),
    ]
