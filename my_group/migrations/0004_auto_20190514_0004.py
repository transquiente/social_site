# Generated by Django 2.2.1 on 2019-05-13 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_group', '0003_auto_20190511_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['-create_data']},
        ),
    ]
