# Generated by Django 3.1.7 on 2021-03-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonebook',
            name='city',
            field=models.CharField(choices=[('Бишкек', 'Бишкек'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Каракол', 'Каракол'), ('Жалал-Абад', 'Жалал-Абад'), ('Баткен', 'Баткен'), ('Талас', 'Талас')], default='Бишкек', max_length=30, verbose_name='Город проживания'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(choices=[('Бишкек', 'Бишкек'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Каракол', 'Каракол'), ('Жалал-Абад', 'Жалал-Абад'), ('Баткен', 'Баткен'), ('Талас', 'Талас')], default='Бишкек', max_length=25, verbose_name='Country'),
        ),
    ]