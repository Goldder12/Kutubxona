# Generated by Django 5.0.7 on 2024-07-19 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('asosiy', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ustoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('jinsi', models.CharField(max_length=30)),
                ('yoshi', models.SmallIntegerField()),
                ('daraja', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('aktive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Universitet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app0813.fan')),
                ('ustoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app0813.ustoz')),
                ('yonalish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app0813.yonalish')),
            ],
        ),
        migrations.AddField(
            model_name='fan',
            name='yonalish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app0813.yonalish'),
        ),
    ]
