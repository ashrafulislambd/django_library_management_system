# Generated by Django 4.2.11 on 2024-06-15 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrowings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(default='2024-01-01'),
        ),
    ]