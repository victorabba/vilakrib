# Generated by Django 4.0 on 2022-01-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vialpi', '0004_alter_contactus_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
