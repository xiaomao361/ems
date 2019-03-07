# Generated by Django 2.1.7 on 2019-03-07 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0030_auto_20190307_0954'),
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
    ]
