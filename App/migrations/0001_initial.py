# Generated by Django 4.2.5 on 2023-09-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=40)),
                ('price', models.CharField(max_length=10)),
                ('qty', models.CharField(max_length=10)),
            ],
        ),
    ]
