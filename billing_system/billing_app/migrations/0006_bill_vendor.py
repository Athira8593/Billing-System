# Generated by Django 4.1.6 on 2023-02-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_app', '0005_rename_user_bill_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='vendor',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
