# Generated by Django 2.2 on 2019-12-14 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191215_0149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='body',
            new_name='summary',
        ),
    ]
