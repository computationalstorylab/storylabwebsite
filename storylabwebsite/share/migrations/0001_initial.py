# Generated by Django 2.2.3 on 2019-07-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OnlineAppendices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('associatedpaper', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=200)),
                ('images', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('abstract', models.IntegerField(default=0)),
                ('body', models.IntegerField(default=0)),
                ('citations', models.IntegerField(default=0)),
            ],
        ),
    ]