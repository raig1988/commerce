# Generated by Django 4.1 on 2022-08-24 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auctionlisting_last_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=20),
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
