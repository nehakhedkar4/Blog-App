# Generated by Django 4.1.3 on 2022-11-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_undopost_id_alter_undopost_undo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='undopost',
            name='undo_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]