# Generated by Django 5.1 on 2024-09-29 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wc', '0002_blockboard_postid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockboard',
            name='postid',
            field=models.IntegerField(null=True),
        ),
    ]
