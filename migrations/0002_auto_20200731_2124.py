# Generated by Django 3.0.8 on 2020-07-31 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertising', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platforms',
            name='budget',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='platforms',
            name='budgetperiod',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='platforms',
            name='extrainfo',
            field=models.CharField(default=None, max_length=300),
        ),
    ]
