# Generated by Django 4.2 on 2023-05-19 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_watchlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='user',
            new_name='bidder',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.AlterField(
            model_name='bid',
            name='listing',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='auctions.listing'),
        ),
    ]
