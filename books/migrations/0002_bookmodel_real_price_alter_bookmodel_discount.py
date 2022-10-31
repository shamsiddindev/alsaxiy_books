# Generated by Django 4.1.2 on 2022-10-31 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='real_price',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='discount',
            field=models.SmallIntegerField(default=0),
        ),
    ]
