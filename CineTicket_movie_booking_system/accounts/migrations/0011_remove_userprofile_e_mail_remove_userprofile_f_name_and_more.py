# Generated by Django 4.2.2 on 2023-11-02 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_rename_user_name_userprofile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='e_mail',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]
