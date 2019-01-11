# Generated by Django 2.0 on 2019-01-10 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0004_auto_20190110_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turns',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='match_turns', to='match.Match'),
        ),
        migrations.AlterField(
            model_name='turns',
            name='play_player1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='card1_turns', to='cards.Card'),
        ),
        migrations.AlterField(
            model_name='turns',
            name='play_player2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='card2_turns', to='cards.Card'),
        ),
        migrations.AlterField(
            model_name='turns',
            name='statut',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='turns',
            name='winner_turns',
            field=models.IntegerField(default=0, null=True),
        ),
    ]