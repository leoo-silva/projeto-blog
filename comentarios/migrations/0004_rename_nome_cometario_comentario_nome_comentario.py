# Generated by Django 3.2.9 on 2021-12-07 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_rename_cometario_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='nome_cometario',
            new_name='nome_comentario',
        ),
    ]
