# Generated by Django 2.0 on 2020-07-14 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('E_R_P_students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RenameModel(
            old_name='Question',
            new_name='Users',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AddField(
            model_name='students',
            name='Users_text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_R_P_students.Users'),
        ),
    ]
