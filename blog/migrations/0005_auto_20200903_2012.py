# Generated by Django 3.1 on 2020-09-03 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200903_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='c_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='c_created_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='c_published_date',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='c_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='c_title',
            new_name='title',
        ),
    ]