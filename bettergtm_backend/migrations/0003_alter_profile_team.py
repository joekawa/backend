# Generated by Django 4.2.16 on 2024-12-03 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bettergtm_backend', '0002_customer_rename_fiirst_name_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bettergtm_backend.team'),
        ),
    ]
