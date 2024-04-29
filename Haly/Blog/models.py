from django.db import models
from ckeditor.fields import RichTextField
from django.contrib import admin


class ReadonlySlugField(models.SlugField):
    def formfield(self, **kwargs):
        kwargs["widget"] = admin.widgets.AdminTextInputWidget(attrs={"readonly": True})
        return super().formfield(**kwargs)

class BlogModel(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False, unique=True, verbose_name='Blogyn ady (TM)')
    title_ru = models.CharField(max_length=500, blank=False, null=False, unique=True, verbose_name='Загаловок (RU)')
    title_en = models.CharField(max_length=500, blank=False, null=False, unique=True, verbose_name='Title (EN)')

    short_description = models.CharField(max_length=1000, blank=False, null=False,
                                         verbose_name='Blog barada gysgaca maglumat (TM)')
    short_description_ru = models.CharField(max_length=1000, blank=False, null=False,
                                            verbose_name='Краткое описание (RU)')
    short_description_en = models.CharField(max_length=1000, blank=False, null=False,
                                            verbose_name='Short description (EN)')

    text = RichTextField(blank=False, null=False, verbose_name='Blogyn beryany (TM)')
    text_ru = RichTextField(blank=False, null=False, verbose_name='Описание блога (RU)')
    text_en = RichTextField(blank=False, null=False, verbose_name='Description of blog (EN)')

    istop = models.BooleanField(default=False, verbose_name="Esasy habarmy")
    image = models.ImageField(upload_to='Blog/%Y-%m-%d', verbose_name='Surat')
    date = models.DateTimeField(auto_now_add=True)

    slug_title = models.SlugField(max_length=500, allow_unicode=True, verbose_name='Degmeli Dal!!!', default='')
    slug_title_ru = models.SlugField(max_length=500, allow_unicode=True, verbose_name='Ничего не писать!!!', default='')
    slug_title_en = models.SlugField(max_length=500, allow_unicode=True, verbose_name='Dont touch!!!', default='')

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
        return f'/blog/post/{self.slug_title}'

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
