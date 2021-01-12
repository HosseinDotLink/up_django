from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class master(models.Model):
    FIELDS = (
        ('m','مدیر گروه'),
        ('h','هیئت علمی'),
        ('k','کارمند یا استاد'),
    )
    master_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    master_picture = models.ImageField(upload_to='master/picture', verbose_name="تصویر",  default='default.jpg')
    master_email = models.EmailField(verbose_name="ایمیل")
    master_phone = models.BigIntegerField(null=True, blank=True, verbose_name="شماره تماس")
    master_website = models.URLField(null=True, blank=True, verbose_name="صفحه شخصی")

    master_level = models.CharField(max_length=50, verbose_name="مرتبه علمی")
    master_degree = models.CharField(max_length=50, verbose_name="آخرین مدرک تحصیلی")
    master_degree_uni = models.CharField(max_length=50, verbose_name="محل اخذ آخرین مدرک تحصیلی")
    master_degree_year = models.PositiveSmallIntegerField(verbose_name="سال اخذ مدرک تحصیلی")

    master_slug = models.SlugField(verbose_name="آدرس صفحه")
    master_status = models.CharField(max_length=1, choices=FIELDS, verbose_name="وضعیت")

    def __str__(self):
        return self.master_name

    class Meta:
        verbose_name= "کارکنان"

    def get_absolute_url(self):
        return reverse('master_detail_view', args=[self.master_slug])


class thesis(models.Model):
    name = models.CharField(max_length=200, verbose_name="عنوان پایان نامه")
    student = models.CharField(max_length=200, verbose_name="دانشجو")
    section = models.CharField(max_length=30, verbose_name="مقطع تحصیلی")
    master = models.CharField(max_length=200, verbose_name="استاد راهنما")
    date = models.DateField(verbose_name="تاریخ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="پایان نامه ها"


class publisher(models.Model):

    FIELDS = (
        ('e','مقاله انگلیسی'),
        ('f','مقاله فارسی'),
        ('k','کتاب'),
    )
    name = models.CharField(max_length=200, verbose_name="عنوان پایان نامه")
    student = models.CharField(max_length=200, verbose_name="دانشجو")
    section = models.CharField(max_length=30, verbose_name="مقطع تحصیلی")
    master = models.CharField(max_length=200, verbose_name="استاد راهنما")
    date = models.DateField(verbose_name="تاریخ")
    status = models.CharField(max_length=1, choices=FIELDS, verbose_name="وضعیت")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="انتشارات"


class release(models.Model):
    rls_name = models.CharField(max_length=200, verbose_name="عنوان طرح")
    rls_topic = models.CharField(max_length=200, verbose_name="نوع طرح")
    rls_presenters = models.CharField(max_length=30, verbose_name="مجریان طرح")

    def __str__(self):
        return self.rls_name

    class Meta:
        verbose_name="طرح های پژوهشی جاری"


class news(models.Model):
    title = models.CharField(max_length=250, verbose_name="موضوع")
    image = models.ImageField(upload_to='news', verbose_name="عکس", default='default.jpg')
    slug = models.SlugField(max_length=250, verbose_name="آدرس")
    body = models.TextField(verbose_name="متن")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    objects = models.Manager()
    class Meta:
        ordering = ('-publish',)
        verbose_name="اخبار"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newsDetail', args=[self.slug])


class notification(models.Model):
    title = models.CharField(max_length=250, verbose_name="موضوع")
    image = models.ImageField(upload_to='notifications', verbose_name="عکس", default='default.jpg')
    slug = models.SlugField(max_length=250, verbose_name="آدرس")
    body = models.TextField(verbose_name="متن")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")

    objects = models.Manager()

    class Meta:
        ordering = ('-publish',)
        verbose_name="اطلاعیه ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notificationsDetail', args=[self.slug])


class event(models.Model):
    title = models.CharField(max_length=250, verbose_name="موضوع")
    image = models.ImageField(upload_to='events', verbose_name="عکس", default='default.jpg')
    slug = models.SlugField(max_length=250, verbose_name="آدرس")
    body = models.TextField(verbose_name="متن")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")

    objects = models.Manager()

    class Meta:
        ordering = ('-publish',)
        verbose_name="رویدادها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('eventsDetail', args=[self.slug])


class lab(models.Model):

    FIELDS = (
        ('p','تخصصی'),
        ('o','عمومی'),
    )
    name = models.CharField(max_length=200, verbose_name="نام آزمایشگاه")
    image = models.ImageField(upload_to= 'labs', verbose_name="عکس آزمایشگاه", default='default.jpg')
    body = models.TextField(verbose_name="توضیحات")
    status = models.CharField(max_length=1, choices=FIELDS, verbose_name="وضعیت")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="آزمایشگاه ها"