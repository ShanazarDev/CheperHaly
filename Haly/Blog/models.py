from django.db import models
from ckeditor.fields import RichTextField


class BlogModel(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False, unique=True, verbose_name='Blogyn ady')
    title_ru = models.CharField(max_length=500, blank=False, null=False, unique=True, verbose_name='Загаловок')
    title_en = models.CharField(max_length=500, blank=False, null=False, unique=True, verbose_name='Title')

    short_description = models.CharField(max_length=1000, blank=False, null=False,
                                         verbose_name='Blog barada gysgaca maglumat')
    short_description_ru = models.CharField(max_length=1000, blank=False, null=False,
                                            verbose_name='Краткое описание')
    short_description_en = models.CharField(max_length=1000, blank=False, null=False,
                                            verbose_name='Short description')

    text = RichTextField(blank=False, null=False, verbose_name='Blogyn beryany')
    text_ru = RichTextField(blank=False, null=False, verbose_name='Описание блога')
    text_en = RichTextField(blank=False, null=False, verbose_name='Description of blog')

    istop = models.BooleanField(default=False, verbose_name="Esasy habarmy")
    image = models.ImageField(upload_to='Blog/%Y-%m-%d', verbose_name='Surat')
    date = models.DateTimeField(auto_now_add=True)

    slug_title = models.SlugField(allow_unicode=True, verbose_name='Degmeli Dal!!!')
    slug_title_ru = models.SlugField(allow_unicode=True, verbose_name='Ничего не писать!!!')
    slug_title_en = models.SlugField(allow_unicode=True, verbose_name='Dont touch!!!')

    views_count = models.BooleanField(default=False, verbose_name='Количество просмотров')

    meta_tags_keywords = models.CharField(max_length=1000, default='', null=True,
                                          verbose_name='Ключевые слова для посиковика',
                                          help_text='Записываете всечерез запятную (,)!!!')

    def image_to_admin(self):
        from django.utils.safestring import mark_safe
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    image_to_admin.short_description = 'Image'
    image_to_admin.allow_tags = True

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'


class BlogViewsModel(models.Model):
    blog_foreign = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='blog_ip')
    views_ip = models.GenericIPAddressField(verbose_name='Ip addres')

    class Meta:
        verbose_name = 'Blog просмотры'
        verbose_name_plural = 'Блог просмотры'
