# Generated by Django 3.1.7 on 2021-03-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210314_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADM', 'Administrator'), ('MNG', 'Manager'), ('GST', 'Guest')], default='Manager', max_length=20, verbose_name='Position'),
        ),
    ]
