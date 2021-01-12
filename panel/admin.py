from django.contrib import admin
from .models import *


class msgAdmin(admin.ModelAdmin):
    list_display = ('msg_master','msg_student','msg_time')
    list_filter = ('msg_master','msg_student','msg_time','msg_master_sender')
    search_fields = ('msg_master','msg_sender','msg_body')
    ordering = ['msg_time', 'msg_master','msg_student']


admin.site.register(message,msgAdmin)


class prjAdmin(admin.ModelAdmin):
    list_display = ('prj_master','prj_student','prj_time')
    list_filter = ('prj_master','prj_student','prj_time','prj_accept')
    search_fields = ('prj_master','prj_sender','prj_title')
    ordering = ['prj_time', 'prj_master','prj_student']


admin.site.register(project,prjAdmin)