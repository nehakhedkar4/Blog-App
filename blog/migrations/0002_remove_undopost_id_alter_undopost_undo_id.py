# Generated by Django 4.1.3 on 2022-11-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='undopost',
            name='id',
        ),
        migrations.AlterField(
            model_name='undopost',
            name='undo_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
