# Generated by Django 5.1.3 on 2024-11-19 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevo_pages', '0005_alter_pagemenu_options_article_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='page',
            name='menu_order',
        ),
        migrations.AddField(
            model_name='page',
            name='is_reverse',
            field=models.BooleanField(default=False, verbose_name='Is reverse'),
        ),
        migrations.AddField(
            model_name='page',
            name='url_path',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL path'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='page',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='page',
            name='meta_custom',
            field=models.TextField(blank=True, null=True, verbose_name='Meta custom tags'),
        ),
        migrations.AlterField(
            model_name='page',
            name='meta_description',
            field=models.CharField(blank=True, max_length=160, null=True, verbose_name='Meta description'),
        ),
        migrations.AlterField(
            model_name='page',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='page',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='pagearticle',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sevo_pages.article', verbose_name='Article'),
        ),
        migrations.AlterField(
            model_name='pagearticle',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='pagearticle',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='pagemenu',
            name='is_reverse',
            field=models.BooleanField(default=False, verbose_name='Is reverse'),
        ),
        migrations.AlterField(
            model_name='pagemenu',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='pagemenu',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sevo_pages.page', verbose_name='Page'),
        ),
        migrations.AlterField(
            model_name='pagemenu',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='pagemenu',
            name='url_path',
            field=models.SlugField(blank=True, null=True, verbose_name='URL path'),
        ),
    ]