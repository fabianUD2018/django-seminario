# Generated by Django 2.1.2 on 2018-10-26 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platillo', '0003_auto_20181026_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platillo',
            name='ingredientes',
            field=models.ManyToManyField(to='platillo.Ingrediente'),
        ),
    ]
