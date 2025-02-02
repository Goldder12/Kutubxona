# Generated by Django 5.0.7 on 2024-07-17 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kutubxonachi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('yosh', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('yosh', models.SmallIntegerField()),
                ('tirik', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Oquvchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('guruh', models.SmallIntegerField()),
                ('yosh', models.SmallIntegerField()),
                ('yonalish', models.CharField(max_length=30)),
                ('bitiruvchi', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('janr', models.CharField(max_length=30)),
                ('sahifa', models.SmallIntegerField()),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2007.muallif')),
            ],
        ),
        migrations.CreateModel(
            name='Kutubxona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olgan_vaqt', models.DateField()),
                ('qaytarish_vaqti', models.DateField(blank=True, null=True)),
                ('qaytargan', models.BooleanField()),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2007.kitob')),
                ('kutubxonachi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2007.kutubxonachi')),
                ('oquvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2007.oquvchi')),
            ],
        ),
    ]
