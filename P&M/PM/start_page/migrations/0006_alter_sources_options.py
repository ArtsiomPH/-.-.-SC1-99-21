# Generated by Django 4.0 on 2022-04-06 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start_page', '0005_sources'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sources',
            options={'ordering': ['source_name'], 'verbose_name': 'Источник', 'verbose_name_plural': 'Источники'},
        ),
    ]
