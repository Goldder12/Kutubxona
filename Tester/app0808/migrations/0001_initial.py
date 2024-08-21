# Generated by Django 5.0.7 on 2024-08-16 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tododescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malumot', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Todostatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faol', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Todotime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaqt', models.DateField()),
            ],
        ),
    ]
