# Generated by Django 4.0 on 2022-04-09 13:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('start_page', '0002_alter_medcine_options_alter_synonyms_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_counter',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата запроса'),
        ),
    ]
