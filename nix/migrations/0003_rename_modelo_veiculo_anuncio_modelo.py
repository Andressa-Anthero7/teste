# Generated by Django 3.2.4 on 2021-06-21 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nix', '0002_alter_anuncio_marca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='modelo_veiculo',
            new_name='modelo',
        ),
    ]