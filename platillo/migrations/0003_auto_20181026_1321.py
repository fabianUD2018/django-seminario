# Generated by Django 2.1.2 on 2018-10-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platillo', '0002_auto_20181026_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platillo',
            name='ingredientes',
            field=models.ManyToManyField(related_name='ingrediente', to='platillo.Ingrediente'),
        ),
    ]
