# Generated by Django 3.0.8 on 2020-08-30 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20200829_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletteruser',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]