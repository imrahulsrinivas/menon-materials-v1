# Generated by Django 3.2 on 2021-05-11 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materials', '0006_materialrequest_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierQuotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('date_of_supply', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials_supplierquotation_created_by', to=settings.AUTH_USER_MODEL)),
                ('material_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials_supplierquotation_material_request', to='materials.materialrequest')),
            ],
        ),
    ]
