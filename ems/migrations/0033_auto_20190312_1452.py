# Generated by Django 2.1.7 on 2019-03-12 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0032_auto_20190312_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='brand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ems.Brand', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='historicalequipment',
            name='brand',
            field=models.ForeignKey(blank=True, db_constraint=False, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ems.Brand', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='openapp',
            name='app_id',
            field=models.CharField(max_length=128, unique=True, verbose_name='app_id'),
        ),
        migrations.AlterField(
            model_name='openapp',
            name='app_key',
            field=models.TextField(max_length=256, verbose_name='app_key'),
        ),
    ]
