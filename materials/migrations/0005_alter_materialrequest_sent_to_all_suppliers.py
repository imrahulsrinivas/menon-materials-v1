# Generated by Django 3.2 on 2021-05-10 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_materialrequest_sent_to_all_suppliers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialrequest',
            name='sent_to_all_suppliers',
            field=models.BooleanField(default=False),
        ),
    ]
