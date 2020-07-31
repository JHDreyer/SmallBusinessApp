# Generated by Django 3.0.8 on 2020-07-30 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('price', models.FloatField(max_length=10)),
                ('image', models.ImageField(default=None, upload_to='')),
                ('business', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customer_profile.Business')),
            ],
        ),
    ]