# Generated by Django 4.2.3 on 2023-09-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0008_alter_data_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='registration_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
