# Generated by Django 4.0 on 2023-02-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='google_auth_code',
            field=models.CharField(default='PR4H7J4IQ43SU6EL', max_length=16),
            preserve_default=False,
        ),
    ]
