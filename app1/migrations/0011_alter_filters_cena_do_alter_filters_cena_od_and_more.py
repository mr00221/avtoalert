# Generated by Django 4.1.4 on 2022-12-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_filters_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filters',
            name='cena_do',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='filters',
            name='cena_od',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='filters',
            name='letnik_do',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='filters',
            name='letnik_od',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='filters',
            name='model',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='filters',
            name='znamka',
            field=models.CharField(default=None, max_length=255),
        ),
    ]