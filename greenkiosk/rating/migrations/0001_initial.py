# Generated by Django 4.2.1 on 2023-06-30 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('review_message', models.TextField()),
                ('sender', models.CharField(max_length=32)),
                ('star_rating', models.DecimalField(decimal_places=2, max_digits=10)),
                ('value', models.CharField(max_length=32)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
