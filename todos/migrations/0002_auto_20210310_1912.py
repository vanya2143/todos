# Generated by Django 3.1.7 on 2021-03-10 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-created']},
        ),
    ]
