# Generated by Django 5.0.7 on 2024-07-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=255)),
                ('year', models.DateField()),
                ('price', models.PositiveBigIntegerField()),
            ],
        ),
    ]
