# Generated by Django 2.0 on 2019-01-10 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_auto_20190110_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turns',
            name='match',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='match_turns', to='match.Match'),
        ),
    ]
