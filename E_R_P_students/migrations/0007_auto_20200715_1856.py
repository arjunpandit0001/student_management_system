# Generated by Django 2.0 on 2020-07-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_R_P_students', '0006_queries'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='Branch',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='Father_name',
            new_name='father_name',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='Phone_no',
            new_name='phone_no',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='User_name',
            new_name='USER_NAME',
        ),
        migrations.AddField(
            model_name='users',
            name='PASSWORD',
            field=models.CharField(default='KIET123', max_length=250),
        ),
    ]