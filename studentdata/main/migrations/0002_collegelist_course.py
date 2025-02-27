# Generated by Django 5.1.6 on 2025-02-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collegelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegename', models.CharField(max_length=150)),
                ('amount', models.IntegerField(null=True)),
                ('enrollmentdate', models.DateField()),
                ('level', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=150)),
                ('amount', models.IntegerField(null=True)),
                ('Image', models.ImageField(upload_to='')),
                ('level', models.CharField(max_length=150)),
            ],
        ),
    ]
