from django.shortcuts import render , get_object_or_404
from .models import event, news, notification, master, lab, publisher, thesis

# Create your views here.
def indexView(request):
    newsList = news.objects.all()[:4]
    eventsList = event.objects.all()[:6]
    notificationsList = notification.objects.all()[:6]
    return render(request, 'index.html', {'news': newsList, 'notifications': notificationsList, 'events':eventsList})


def newsDetail(request, newsSlug):
    data = get_object_or_404(news, slug=newsSlug)
    return render(request, 'detail.html', {'data': data})


def newsList(request):
    title = "اخبار"
    data = news.objects.all()
    return render(request, 'newsList.html', {'data': data, 'title': title})


def notificationList(request):
    title = "اطلاعیه های"
    data = notification.objects.all()
    return render(request, 'newsList.html', {'data': data, 'title': title})


def eventList(request):
    title = "رویداد های"
    data = event.objects.all()
    return render(request, 'newsList.html', {'data': data, 'title': title})


def eventsDetail(request, eventSlug):
    data = get_object_or_404(event, slug=eventSlug)
    return render(request, 'detail.html', {'data': data})


def notificationsDetail(request, ntfSlug):
    data = get_object_or_404(notification, slug=ntfSlug)
    return render(request, 'detail.html', {'data': data})

def masterHGS(request):
    title = "مدیر گروه کامپیوتر دانشگاه تربت حیدریه"
    masterList = master.objects.filter(master_status='m')
    return render(request, 'memberList.html', {'masterList': masterList, 'title':title})


def masterSC(request):
    title = "اعضای هیئت علمی گروه کامپیوتر دانشگاه تربت حیدریه"
    masterList = master.objects.filter(master_status='h')
    return render(request, 'memberList.html', {'masterList': masterList, 'title':title})


def masterStaff(request):
    title = "کارکنان گروه کامپیوتر دانشگاه تربت حیدریه"
    masterList = master.objects.filter(master_status='k')
    return render(request, 'memberList.html', {'masterList': masterList, 'title':title})


def bachelor(request):
    title = "اطلاعات مقطع کارشناسی گروه کامپیوتر دانشگاه تربت حیدریه"
    return render(request, 'KarshenasiAmPage.html', {'title':title})


def assistant(request):
    title = "اطلاعات مقطع کاردانی گروه کامپیوتر دانشگاه تربت حیدریه"
    return render(request, 'KardaniAmPage.html', {'title': title})


def generalLabs(request):
    title = "آزمایشگاه های عمومی گروه کامپیوتر دانشگاه تربت حیدریه"
    labs = lab.objects.filter(status='o')
    return render(request, 'Lab.html', {'labs': labs, 'title':title})


def professionalLabs(request):
    title = "آزمایشگاه های تخصصی گروه کامپیوتر دانشگاه تربت حیدریه"
    labs = lab.objects.filter(status='p')
    return render(request, 'Lab.html', {'labs': labs, 'title':title})


def thesisGuide(request):
    title = "راهنمای تهیه پایان نامه گروه کامپیوتر دانشگاه تربت حیدریه"
    return render(request, 'thesisGuide.html', {'title': title})


def englishPub(request):
    title = "مقالات انگلیسی منتشر شده گروه کامپیوتر دانشگاه تربت حیدریه"
    pubs = publisher.objects.filter(status='e')
    return render(request, 'PayanPage.html', {'data': pubs, 'title':title, 'en': True})


def persianPub(request):
    title = "مقالات منتشر شده گروه کامپیوتر دانشگاه تربت حیدریه"
    pubs = publisher.objects.filter(status='f')
    return render(request, 'PayanPage.html', {'data': pubs, 'title':title})


def bookPub(request):
    title = "کتاب های منتشر شده گروه کامپیوتر دانشگاه تربت حیدریه"
    pubs = publisher.objects.filter(status='k')
    return render(request, 'PayanPage.html', {'data': pubs, 'title':title})


def thesisList(request):
    title = "پایان نامه های دفاع شده گروه کامپیوتر دانشگاه تربت حیدریه"
    pubs = thesis.objects.filter()
    return render(request, 'PayanPage.html', {'data': pubs, 'title':title})