# Generated by Django 2.0 on 2020-07-17 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_R_P_students', '0010_auto_20200717_2327'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='queries',
            new_name='quires',
        ),
        migrations.AddField(
            model_name='students',
            name='ACTIVE_STATUS',
            field=models.CharField(default='ACTIVE', max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='USER_NAME',
            field=models.CharField(default='', max_length=200),
        ),
    ]