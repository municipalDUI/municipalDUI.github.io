# Generated by Django 4.2.15 on 2024-08-15 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_alter_question_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='tite',
            new_name='title',
        ),
    ]
