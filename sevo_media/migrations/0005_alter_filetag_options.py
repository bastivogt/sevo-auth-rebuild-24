# Generated by Django 5.1.3 on 2024-11-20 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sevo_media', '0004_filetag_alter_picturetag_options_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filetag',
            options={'ordering': ['-updated_at'], 'verbose_name': 'File Tag', 'verbose_name_plural': 'File Tags'},
        ),
    ]