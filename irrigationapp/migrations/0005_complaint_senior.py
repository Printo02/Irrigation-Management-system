# Generated by Django 4.1.1 on 2023-04-12 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('irrigationapp', '0004_complaint_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='senior',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='irrigationapp.sengineer'),
        ),
    ]
