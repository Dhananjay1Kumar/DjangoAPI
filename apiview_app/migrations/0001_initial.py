# Generated by Django 2.2.10 on 2020-03-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('enam', models.CharField(max_length=30)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=200)),
            ],
        ),
    ]