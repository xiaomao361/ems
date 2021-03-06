# Generated by Django 2.1.7 on 2019-02-27 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('sn', models.CharField(max_length=128, unique=True)),
                ('img', models.CharField(max_length=256)),
                ('state', models.CharField(choices=[('unused', '库存'), ('useing', '使用中'), ('fixing', '维修中'), ('scrap', '报废')], default='库存', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['-c_time'],
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-c_time'], 'verbose_name': '分类', 'verbose_name_plural': '分类'},
        ),
        migrations.AddField(
            model_name='equipment',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ems.Category'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ems.User'),
        ),
    ]
