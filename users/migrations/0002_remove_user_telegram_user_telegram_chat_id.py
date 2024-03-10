# Generated by Django 4.2.7 on 2024-03-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='telegram',
        ),
        migrations.AddField(
            model_name='user',
            name='telegram_chat_id',
            field=models.CharField(default=1, max_length=50, verbose_name='Telegram chat ID'),
            preserve_default=False,
        ),
    ]