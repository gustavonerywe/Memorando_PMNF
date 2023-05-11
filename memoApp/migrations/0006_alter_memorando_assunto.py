# Generated by Django 4.1.7 on 2023-05-11 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memoApp', '0005_rename_corpo_memorando_memorando_corpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memorando',
            name='assunto',
            field=models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='memoApp.image', verbose_name='Digite o assunto'),
        ),
    ]
