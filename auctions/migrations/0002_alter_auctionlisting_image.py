# Generated by Django 4.1 on 2022-08-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads'),
        ),
    ]