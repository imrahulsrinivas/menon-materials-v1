# Generated by Django 3.2 on 2021-05-11 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0008_auto_20210511_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierquotation',
            name='quote_status',
            field=models.CharField(choices=[('not_approved', 'NOT APPROVED'), ('approved', 'APPROVED'), ('goods_dispatched', 'GOODS_DISPATCHED')], default='not_approved', max_length=100),
        ),
    ]
