# Generated by Django 2.1.7 on 2019-03-05 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0025_auto_20190305_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='brand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ems.Brand', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='user',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='ems.User', verbose_name='使用人'),
        ),
        migrations.AlterField(
            model_name='historicalequipment',
            name='brand',
            field=models.ForeignKey(blank=True, db_constraint=False, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ems.Brand', verbose_name='品牌'),
        ),
    ]
