# Generated by Django 4.0.5 on 2022-06-18 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]