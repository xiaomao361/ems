# Generated by Django 2.1.7 on 2019-03-13 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0036_auto_20190313_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='bakdata',
            name='size',
            field=models.CharField(default='', max_length=128, verbose_name='size'),
        ),
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