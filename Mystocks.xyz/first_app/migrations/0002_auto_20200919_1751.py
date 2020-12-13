# Generated by Django 2.2 on 2020-09-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='Beta',
        ),
        migrations.RemoveField(
            model_name='info',
            name='EPS',
        ),
        migrations.RemoveField(
            model_name='info',
            name='Earnings_Date',
        ),
        migrations.RemoveField(
            model_name='info',
            name='Forward_Dividend',
        ),
        migrations.RemoveField(
            model_name='info',
            name='Market_Cap',
        ),
        migrations.RemoveField(
            model_name='info',
            name='PE_Ratio',
        ),
        migrations.AddField(
            model_name='info',
            name='Price',
            field=models.CharField(default='', max_length=50, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='info',
            name='Ticker',
            field=models.CharField(default='', max_length=50, verbose_name='Тикер'),
        ),
        migrations.AddField(
            model_name='info',
            name='div_year',
            field=models.CharField(default='', max_length=50, verbose_name='Дивиденды в год'),
        ),
        migrations.AddField(
            model_name='info',
            name='div_year_quarter',
            field=models.CharField(default='', max_length=50, verbose_name='Деведенды в квартал'),
        ),
    ]
