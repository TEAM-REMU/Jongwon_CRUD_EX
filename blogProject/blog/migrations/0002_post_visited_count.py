# Generated by Django 3.0.8 on 2020-07-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visited_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
