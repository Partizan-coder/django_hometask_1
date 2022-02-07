# Generated by Django 4.0.2 on 2022-02-07 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_section_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlerelevance',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='articles.section', verbose_name='Название раздела'),
        ),
    ]
