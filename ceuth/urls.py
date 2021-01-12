"""ceuth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexView, name='index'),
    path('news/<newsSlug>/', views.newsDetail, name='newsDetail'),
    path('news/', views.newsList, name='newsList'),
    path('events/', views.eventList, name='eventList'),
    path('notifications/', views.notificationList, name='notificationList'),
    path('events/<eventSlug>/', views.eventsDetail, name='eventsDetail'),
    path('notifications/<ntfSlug>/', views.notificationsDetail, name='notificationsDetail'),
    path('panel/', include('panel.urls') ),
    path('master/hgs', views.masterHGS, name='masterHGS'),
    path('master/sc', views.masterSC, name='masterSC'),
    path('master/staff', views.masterStaff, name='masterStaff'),
    path('bachelor/', views.bachelor, name='bachelor'),
    path('assistant/', views.assistant, name='assistant'),
    path('lab/general', views.generalLabs, name='generalLabs'),
    path('lab/professional', views.professionalLabs, name='professionalLabs'),
    path('thesis/guide', views.thesisGuide, name='thesisGuide'),
    path('pub/en', views.englishPub, name='englishPub'),
    path('pub/fa', views.persianPub, name='persianPub'),
    path('pub/books', views.bookPub, name='bookPub'),
    path('thesis/', views.thesisList, name='thesisList'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

