from django.db import models
from ckeditor.fields import RichTextField


class NewsModel(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False, unique=True, verbose_name='Habaryn ady (TM)')
    title_ru = models.CharField(max_length=500, blank=False, null=False, unique=True, verbose_name='Загаловок (RU)')
    title_en = models.CharField(max_length=500, blank=False, null=False, unique=True, verbose_name='Title (EN)')

    short_description = models.CharField(max_length=1000, blank=False, null=False,
                                         verbose_name='Habar barada gysgaca maglumat (TM)')
    short_description_ru = models.CharField(max_length=1000, blank=False, null=False,
                                            verbose_name='Краткое описание (RU)')
    short_description_en = models.CharField(max_length=1000, blank=False, null=False,
                                            verbose_name='Short description (EN)')

    text = RichTextField(blank=False, null=False, verbose_name='Habaryn beryany (TM)')
    text_ru = RichTextField(blank=False, null=False, verbose_name='Описание новостя (RU)')
    text_en = RichTextField(blank=False, null=False, verbose_name='Description of news (EN)')

    istop = models.BooleanField(default=False, verbose_name="Esasy habarmy")
    image = models.ImageField(upload_to='News/%Y-%m-%d', verbose_name='Surat')
    date = models.DateTimeField(auto_now_add=True)

    slug_title = models.SlugField(max_length=500, allow_unicode=True, verbose_name='Degmeli Dal!!!',
                                  help_text='Degmeli Dal!!!')
    slug_title_ru = models.SlugField(max_length=500, allow_unicode=True, verbose_name='Ничего не писать!!!')
    slug_title_en = models.SlugField(max_length=500, allow_unicode=True, verbose_name='Dont touch!!!')

    views_count = models.BooleanField(default=False, verbose_name='Количество просмотров')

    meta_tags_keywords = models.CharField(max_length=1000, default='', null=True, blank=True,
                                          verbose_name='Ключевые слова для посиковика',
                                          help_text='Записываете всечерез запятную (,)!!!')

    def image_to_admin(self):
        from django.utils.safestring import mark_safe
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    image_to_admin.short_description = 'Image'
    image_to_admin.allow_tags = True

    def get_absolute_url(self):
        return f'/news/{self.slug_title}'

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Habarlar'
        verbose_name_plural = 'Habarlar'


class NewsViewModel(models.Model):
    news_post = models.ForeignKey(NewsModel, verbose_name='Новостной пост', on_delete=models.CASCADE,
                                  related_name='news_post')
    ip = models.GenericIPAddressField(verbose_name='Ip address')

    class Meta:
        verbose_name = 'Новости просмотры'
        verbose_name_plural = 'Новости просмотры'
