# Generated by Django 4.0.2 on 2022-02-07 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_scope_scopetitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='scopeTitle',
        ),
    ]
