# Generated by Django 4.2.15 on 2024-08-15 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tite', models.CharField(max_length=60)),
                ('question', models.TextField(max_length=400)),
                ('priotity', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], max_length=1)),
            ],
        ),
    ]
