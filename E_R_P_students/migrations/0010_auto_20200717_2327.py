# Generated by Django 2.0 on 2020-07-17 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_R_P_students', '0009_teacher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='TEACHER_NAME',
            new_name='USER_NAME',
        ),
    ]
