# Generated by Django 4.1.4 on 2022-12-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_filters_znamka'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avti',
            fields=[
                ('carID', models.AutoField(primary_key=True, serialize=False)),
                ('ime', models.CharField(default='', max_length=255)),
                ('cena', models.IntegerField()),
                ('registracija', models.DateField()),
                ('km', models.IntegerField()),
                ('fizicna_os', models.SmallIntegerField()),
                ('poskodovano', models.SmallIntegerField()),
                ('scrapeTime', models.DateTimeField()),
            ],
        ),
    ]