from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class message(models.Model):
    msg_master = models.ForeignKey(User, verbose_name='استاد', related_name='master', on_delete=models.CASCADE)
    msg_student = models.ForeignKey(User, verbose_name='دانشجو', related_name='student', on_delete=models.CASCADE)
    msg_time = models.DateTimeField(default=timezone.now, verbose_name='زمان ارسال')
    msg_master_sender = models.BooleanField(default=False, verbose_name='ارسال کننده استاد است؟')
    msg_body = models.TextField(max_length=500, verbose_name='متن پیام')


    def __str__(self):
        return self.msg_body
    
    class Meta:
        verbose_name='پیام ها'

class project(models.Model):
    prj_master = models.ForeignKey(User, verbose_name='استاد', on_delete=models.CASCADE)
    prj_student = models.CharField(max_length=100,verbose_name='دانشجو', null=True, blank=True)
    prj_time = models.DateTimeField(default=timezone.now, verbose_name='زمان تعریف')
    prj_title = models.TextField(max_length=200, verbose_name='متن پیام')
    prj_accept = models.BooleanField(default=False, verbose_name='تایید نهایی')

    def __str__(self):
        return self.prj_title

    class Meta:
        verbose_name = 'پروژه ها'