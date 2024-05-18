# Generated by Django 5.0.4 on 2024-05-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_video_turi_page2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nomi_K',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Operativka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_turi', models.IntegerField(choices=[(1, 'DDR'), (2, 'DDR2'), (3, 'DDR3'), (4, 'DDR4'), (5, 'DDR5')])),
            ],
        ),
        migrations.CreateModel(
            name='Protsessor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_turi', models.IntegerField(choices=[(3, 'Core 3'), (5, 'Core 5'), (7, 'Core 7'), (9, 'Core 9')])),
            ],
        ),
        migrations.CreateModel(
            name='Ram_xotira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ram_x', models.IntegerField(choices=[(2, '2 GB RAM'), (4, '4 GB RAM'), (8, '8 GB RAM'), (12, '12 GB RAM'), (16, '16 GB RAM'), (24, '24 GB RAM'), (32, '32 GB RAM'), (64, '64 GB RAM'), (128, '128 GB RAM')])),
            ],
        ),
        migrations.CreateModel(
            name='Yadro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yadro_turi', models.IntegerField(choices=[(2, '2 yadro'), (4, '4 yadro'), (6, '6 yadro'), (8, '8 yadro'), (10, '10 yadro'), (12, '12 yadro'), (16, '16 yadro'), (18, '18 yadro'), (24, '24 yadro'), (32, '32 yadro'), (64, '64 yadro')])),
            ],
        ),
    ]
