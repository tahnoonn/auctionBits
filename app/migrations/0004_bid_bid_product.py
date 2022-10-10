# Generated by Django 4.1.1 on 2022-09-20 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_owned_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='Bid for'),
            preserve_default=False,
        ),
    ]