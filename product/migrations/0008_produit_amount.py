# Generated by Django 3.0.5 on 2020-06-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
