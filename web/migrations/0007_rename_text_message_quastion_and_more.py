# Generated by Django 4.1.4 on 2022-12-19 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_eventstack_options_alter_userstack_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='text',
            new_name='quastion',
        ),
        migrations.RemoveField(
            model_name='message',
            name='created_at',
        ),
        migrations.AddField(
            model_name='message',
            name='answer',
            field=models.TextField(default='', verbose_name='Ответ'),
            preserve_default=False,
        ),
    ]
