# Generated by Django 2.0 on 2020-07-15 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('E_R_P_students', '0005_auto_20200715_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='queries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USER_NAME', models.CharField(default='NULL', max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('STATUS', models.CharField(default='NO QUERY', max_length=100)),
                ('query', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='E_R_P_students.students')),
            ],
        ),
    ]
