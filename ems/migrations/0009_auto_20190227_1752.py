# Generated by Django 2.1.7 on 2019-02-27 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0008_auto_20190227_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='brand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ems.Brand'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='img',
            field=models.TextField(max_length=256),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='remark',
            field=models.TextField(default='', max_length=256),
        ),
    ]
