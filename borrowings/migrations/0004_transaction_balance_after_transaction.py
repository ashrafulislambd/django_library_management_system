# Generated by Django 4.2.11 on 2024-06-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrowings', '0003_alter_transaction_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='balance_after_transaction',
            field=models.IntegerField(default=0),
        ),
    ]