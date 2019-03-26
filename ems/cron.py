from ems import models
import requests
import datetime
import time
import os


def add_risk(title, content, level, refer_equ_id):
    risk = models.risk(
        title=title, content=content, level=level, refer_equ_id=refer_equ_id)
    risk.save()
    return "success"


def add_sell(title, content, advice_price, equ_id):
    sell = models.Could_sell(
        title=title, content=content, advice_price=advice_price, equ_id=equ.id)
    sell.save()
    return "success"


def printer_check():
    printer_url = ''
    ret = requests.get(printer_url)
    if ret.status < 20:
        title = "硒鼓即将用尽"
        content = "打印机硒鼓余量不足20%，请及时采购"
        level = 'normal'
        refer_equ_id = '9'
        add_risk(title, content, level, refer_equ_id)


def warranty_check():
    equs = models.Equipment.objects.all()
    today = datetime.date.today()
    for equ in equs:
        if today - equ.c_time > equ.warranty:
            title = "设备已出质保期"
            content = "设备已出质保期，请联系续保"
            level = 'danger'
            add_risk(title, content, level, equ.id)
        elif equ.warranty - (today - equ.c_time) < 30:
            title = "设备质保期不足30天"
            content = "设备质保期不足30天"
            level = 'warning'
            add_risk(title, content, level, equ.id)


def backup_check():
    equs = models.Equipment.objects.filter(state='scrap')
    # do analyze
    title = "请及时做好备份工作"
    content = "近三月内该批次，该品牌设备一出现三次以上硬盘损坏情况"
    level = 'danger'
    equ.id = ""
    add_risk(title, content, level, equ.id)


def backup_data():
    now = time.strftime('%Y%m%d%H%M%S')
    os.system('python manage.py dumpdata --format=json > ./backup/' + now)
    size = os.path.getsize('./backup/' + now)
    models.BakData.objects.create(name=now, size=round(size/1024))


def could_sell_check():
    equs = models.Equipment.objects.all()
    # do analyze
    title = ""
    content = ""
    advice_price = ""
    equ_id = ""
    add_sell(title, content, advice_price, equ_id)
