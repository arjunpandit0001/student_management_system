# Generated by Django 2.0 on 2020-07-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_R_P_students', '0004_auto_20200715_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='question_text',
            new_name='User_name',
        ),
        migrations.AddField(
            model_name='users',
            name='USERTYPE',
            field=models.CharField(default='S', max_length=250),
        ),
    ]
