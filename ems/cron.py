from ems import models
import requests
import datetime
import time
import os


def printer_check():
    printer_url = ''
    ret = requests.get(printer_url)
    if ret.status < 20:
        risk = models.risk(
            title=('硒鼓即将用尽'), content='打印机硒鼓余量不足20%，请及时采购', level='normal', refer_equ_id='9')
        risk.save()


def warranty_check():
    equs = models.Equipment.objects.all()
    today = datetime.date.today()
    for equ in equs:
        if today - equ.c_time > equ.warranty:
            risk = models.risk(
                title=('设备已出质保期'), content='设备已出质保期，请联系续保', level='danger', refer_equ_id=equ.id)
            risk.save()
        elif equ.warranty - (today - equ.c_time) < 30:
            risk = models.risk(
                title=('设备质保期不足30天'), content='设备质保期不足30天', level='warning', refer_equ_id=equ.id)
            risk.save()


def backup_check():
    equs = models.Equipment.objects.filter(state='scrap')
    # do analyze
    risk = models.risk(
        title=('请及时做好备份工作'), content='近三月内该批次，该品牌设备一出现三次以上硬盘损坏情况', level='danger', refer_equ_id=equs.id)
    risk.save()


def backup_data():
    now = time.strftime('%Y%m%d%H%M%S')
    os.system('python manage.py dumpdata --format=json > ./backup/' + now)
    size = os.path.getsize('./backup/' + now)
    models.BakData.objects.create(name=now, size=round(size/1024))

