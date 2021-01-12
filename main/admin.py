from django.contrib import admin
from .models import *
# Register your models here.


class masterAdmin(admin.ModelAdmin):
    list_display = ('master_name','master_level','master_status')
    list_filter = ('master_status','master_level','master_degree','master_degree_uni','master_degree_year')
    search_fields = ('master_name','master_level','master_degree','master_degree_uni')
    prepopulated_fields = {'master_slug': ('master_name',)}
    ordering = ['master_status', 'master_name','master_level']


admin.site.register(master,masterAdmin)


class thesisAdmin(admin.ModelAdmin):
    list_display = ('name','student','master','date')
    list_filter = ('student','section','master','date')
    search_fields = ('name','student','section','master','date')
    ordering = ['date', 'section','name']


admin.site.register (thesis,thesisAdmin)


class publisherAdmin(admin.ModelAdmin):
    list_display = ('name','student','master','date','status')
    list_filter = ('status','student','section','master','date')
    search_fields = ('name','student','section','master','date')
    ordering = ['status','date', 'section','name']


admin.site.register(publisher,publisherAdmin)


class releaseAdmin(admin.ModelAdmin):
    list_display = ('rls_name','rls_topic','rls_presenters')
    list_filter = ('rls_topic','rls_name','rls_presenters')
    search_fields = ('rls_name','rls_topic','rls_presenters')
    ordering = ['rls_topic','rls_name','rls_presenters']


admin.site.register(release,releaseAdmin)


class newsAdmin(admin.ModelAdmin):
    list_display = ('title','publish')
    list_filter = ('publish',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title','slug','body')
    ordering = ['title','publish']


admin.site.register(news,newsAdmin)


class notificationAdmin(admin.ModelAdmin):
    list_display = ('title','publish')
    list_filter = ('publish',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title','slug','body')
    ordering = ['title','publish']


admin.site.register(notification,notificationAdmin)


class eventAdmin(admin.ModelAdmin):
    list_display = ('title','publish')
    list_filter = ('publish',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title','slug','body')
    ordering = ['title','publish']


admin.site.register(event,eventAdmin)


class labsAdmin(admin.ModelAdmin):
    list_display = ('name','status')
    list_filter = ('status',)
    search_fields = ('name','body')
    ordering = ['name','status']


admin.site.register(lab,labsAdmin)