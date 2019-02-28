# Generated by Django 2.1.7 on 2019-02-28 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0013_auto_20190228_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='brand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ems.Brand', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='state',
            field=models.CharField(choices=[('unused', '库存'), ('useing', '使用中'), ('fixing', '维修中'), ('scrap', '报废'), ('problem', '问题')], default='库存', max_length=32, verbose_name='状态'),
        ),
    ]
