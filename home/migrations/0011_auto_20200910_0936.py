# Generated by Django 3.0.8 on 2020-09-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200910_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='lang',
            field=models.CharField(blank=True, choices=[], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='settinglang',
            name='lang',
            field=models.CharField(choices=[], max_length=50),
        ),
    ]
