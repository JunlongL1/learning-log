# Generated by Django 4.0.3 on 2022-03-20 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='date_add',
            new_name='date_added',
        ),
    ]
