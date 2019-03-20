from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords


class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    departments = (
        ('it', "信息部"),
        ('hr', "人力部"),
        ('administrative', "行政部"),
        ('financial', "财务部"),
        ('manager', "总经办"),
        ('sales', "销售部"),
        ('market', "市场部"),
    )

    name = models.CharField(max_length=128, unique=True, verbose_name='用户名')
    full_name = models.CharField(max_length=128, default="", verbose_name='姓名')
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(unique=True, verbose_name='邮件')
    phone = models.CharField(max_length=128, default="", verbose_name='电话')
    sex = models.CharField(max_length=32, choices=gender,
                           default="男", verbose_name='性别')
    department = models.CharField(
        max_length=32, choices=departments, default="", verbose_name='所属部门')
    img = models.CharField(max_length=128, default="", verbose_name='头像')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "员工"
        verbose_name_plural = "员工"


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='类别')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "分类"
        verbose_name_plural = "分类"


class Brand(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='品牌')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "品牌"
        verbose_name_plural = "品牌"


class Equipment(models.Model):
    gender = (
        ('unused', "库存"),
        ('useing', "使用中"),
        ('fixing', "维修中"),
        ('scrap', "报废"),
        ('problem', "问题"),
        ('sell', "卖出"),
    )

    name = models.CharField(max_length=128, unique=True, verbose_name='设备名称')
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name='设备类别',  related_name='category')
    sn = models.CharField(max_length=128, unique=True, verbose_name='SN码/序列号')
    brand = models.ForeignKey(
        'Brand', on_delete=models.CASCADE, default="", verbose_name='品牌')
    img = models.CharField(max_length=256, default="",
                           blank=True, verbose_name='图片地址')
    state = models.CharField(
        max_length=32, choices=gender, default="库存", verbose_name='状态')
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, blank=True, default="", null=True,
        verbose_name='使用人')
    remark = models.TextField(
        max_length=256, default="", blank=True, verbose_name='备注')
    procurement = models.ForeignKey(
        'Merchant', on_delete=models.CASCADE, default="", null=True, verbose_name='采购方')
    price_in = models.CharField(max_length=128, verbose_name='买入价格')
    price_out = models.CharField(
        max_length=128, blank=True, verbose_name='卖出价格')
    maintain = models.ForeignKey('Merchant', on_delete=models.CASCADE, default="null",
                                 blank=True, related_name="fixer", null=True, verbose_name='维修方')
    history = HistoricalRecords()
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "设备"
        verbose_name_plural = "设备"


class Merchant(models.Model):
    gender = (
        ('sell', "销售"),
        ('fixing', "维修"),
        ('recycle', "回收"),
    )
    name = models.CharField(max_length=128, unique=True, verbose_name='商户名称')
    phone = models.CharField(max_length=128, verbose_name='商户电话')
    contact = models.CharField(max_length=128, default="", verbose_name='联系人')
    email = models.CharField(max_length=256, default="",
                             blank=True, verbose_name='邮件地址')
    info = models.TextField(max_length=256, default="",
                            blank=True, verbose_name='店铺信息')
    type = models.CharField(max_length=32, choices=gender, default="")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "商户"
        verbose_name_plural = "商户"


class Notice(models.Model):
    title = models.CharField(max_length=128, unique=True, verbose_name='标题')
    content = models.TextField(
        max_length=256, default="", blank=True, verbose_name='内容')
    is_read = models.BooleanField(default=False, verbose_name='是否已读')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "消息"
        verbose_name_plural = "消息"


class OpenApp(models.Model):
    app_id = models.CharField(max_length=128, unique=True, verbose_name='app_id')
    app_key = models.TextField(max_length=256, verbose_name='app_key')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.app_id

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "app_id"
        verbose_name_plural = "app_id"

class BakData(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='name')
    size = models.CharField(max_length=128, default="", verbose_name='size')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "name"
        verbose_name_plural = "name"

class Joke(models.Model):
    content = models.CharField(max_length=128, unique=True, verbose_name='内容')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-c_time"]