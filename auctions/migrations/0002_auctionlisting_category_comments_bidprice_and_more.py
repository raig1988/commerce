# Generated by Django 4.1 on 2022-08-18 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('start_price', models.FloatField(max_length=20)),
                ('image', models.FileField(null=True, upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.auctionlisting')),
            ],
        ),
        migrations.CreateModel(
            name='BidPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_price', models.FloatField(max_length=20)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lastprice', to='auctions.auctionlisting')),
            ],
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='auctions.category'),
        ),
    ]
