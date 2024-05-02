from django.db import models
from ckeditor.fields import RichTextField
from Blog.models import ReadonlySlugField


class NewsModel(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False, unique=True, verbose_name='Habaryn ady')
    short_description = models.CharField(max_length=1000, blank=False, null=False,
                                         verbose_name='Habar barada gysgaca maglumat')
    text = RichTextField(blank=False, null=False, verbose_name='Habaryn beryany')
    istop = models.BooleanField(default=False, verbose_name="Esasy habarmy")
    image = models.ImageField(upload_to='News/%Y-%m-%d', verbose_name='Surat')
    date = models.DateTimeField(auto_now_add=True)
    slug_title = ReadonlySlugField(max_length=500, allow_unicode=True, verbose_name='Degmeli Dal!!!',
                                   help_text='Degmeli Dal!!!')
    views_count = models.BooleanField(default=False, verbose_name='Habarlaryn gorkezilen sany')
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
    news_post = models.ForeignKey(NewsModel, verbose_name='Habar', on_delete=models.CASCADE,
                                  related_name='news_post')
    ip = models.GenericIPAddressField(verbose_name='Ip address')

    class Meta:
        verbose_name = 'Habaralryn gorlen sany'
        verbose_name_plural = 'Habaralryn gorlen sany'
