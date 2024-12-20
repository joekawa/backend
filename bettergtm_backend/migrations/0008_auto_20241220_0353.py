# Generated by Django 3.0.4 on 2024-12-20 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bettergtm_backend', '0007_auto_20241220_0318'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
        migrations.AddField(
            model_name='goal',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bettergtm_backend.Customer'),
        ),
        migrations.AddField(
            model_name='output',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bettergtm_backend.Customer'),
        ),
        migrations.AddField(
            model_name='release',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bettergtm_backend.Customer'),
        ),
        migrations.AddField(
            model_name='releaseactivity',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bettergtm_backend.Customer'),
        ),
        migrations.AddField(
            model_name='releasetype',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bettergtm_backend.Customer'),
        ),
        migrations.AddField(
            model_name='status',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bettergtm_backend.Customer'),
        ),
        migrations.AddField(
            model_name='team',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bettergtm_backend.Customer'),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
