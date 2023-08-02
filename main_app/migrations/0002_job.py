# Generated by Django 4.2.3 on 2023-08-01 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='Job Date')),
                ('time', models.TimeField(blank=True, verbose_name='Job Time')),
                ('status', models.CharField(choices=[('I', 'Complete'), ('C', 'Incomplete')], default='I', max_length=1)),
            ],
        ),
    ]
