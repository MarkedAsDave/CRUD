# Generated by Django 4.2.5 on 2023-09-21 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=40)),
                ('price', models.CharField(max_length=10)),
                ('qty', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
