# Generated by Django 3.0.5 on 2020-07-02 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200702_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False'), ('Closed', 'Closed')], default='True', max_length=10),
        ),
    ]
