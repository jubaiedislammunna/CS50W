# Generated by Django 5.0.1 on 2024-01-19 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='aurthor',
            new_name='author',
        ),
    ]
