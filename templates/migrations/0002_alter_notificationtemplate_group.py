# Generated by Django 5.0.3 on 2024-04-28 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationtemplate',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='group_templates', to='templates.usergroup'),
        ),
    ]
