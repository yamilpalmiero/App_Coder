# Generated by Django 4.0.3 on 2022-03-28 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0004_remove_curso_id_alter_curso_comision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregable',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
