# Generated by Django 5.0.4 on 2024-05-13 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_tovarslar_s_tur_lar_s_backet_s_tovarslar_s_turi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video_turi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turi', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Page2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('you_tobe_linki', models.CharField(max_length=500)),
                ('nomi', models.CharField(max_length=200)),
                ('turi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.video_turi')),
            ],
        ),
    ]
