# Generated by Django 2.0.4 on 2018-05-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=200)),
                ('grade', models.PositiveIntegerField()),
                ('activity', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=200)),
                ('establish_date', models.DateField()),
                ('logo_url', models.CharField(max_length=200)),
                ('slogan', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('keyword', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('homepage', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]