from django.db import models
from django.utils.safestring import mark_safe


class GalleryModel(models.Model):
    category_choice = (
        ('Category 1', 'Большие ковры'),
        ('Category 2', 'Изделия из ковров'),
        ('Category 3', 'Аксессуары')
    )
    name = models.CharField(max_length=225, blank=True, null=False, verbose_name='Halynyn ady',
                            help_text='Halynyn ady')
    name_ru = models.CharField(max_length=225, blank=True, null=False, verbose_name='Название ковра',
                               help_text='Название ковра')
    name_en = models.CharField(max_length=225, blank=True, null=False, verbose_name='Carpet name',
                               help_text='Carpet name')

    description = models.CharField(max_length=500, blank=True, null=False, verbose_name='Haly barada maglumat',
                                   help_text='Haly barada gysgaca maglumat')
    description_ru = models.CharField(max_length=500, blank=True, null=False, verbose_name='Описание ковра',
                                      help_text='Краткое описанние ковра')
    description_tm = models.CharField(max_length=500, blank=True, null=False, verbose_name='Description for carpet',
                                      help_text='Short description of carpet')

    size_of_carpet = models.CharField(max_length=255, blank=True, null=True, verbose_name='Размер ковара',
                                      help_text='4,5 m x 5 m')

    image = models.ImageField(upload_to='gallery/', verbose_name='Картина')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    category = models.CharField(max_length=50, verbose_name='Категория картиины', blank=False, null=False,
                                choices=category_choice, default='Category 1')

    price = models.IntegerField(verbose_name='Стоисомть ковра', default=0)

    def image_to_admin(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    image_to_admin.short_description = 'Image'
    image_to_admin.allow_tags = True


class GalleryHomeModel(models.Model):
    category_choice = (
        ('tabs-2-1', 'Большие ковры'),
        ('tabs-2-2', 'Изделия из ковров'),
        ('tabs-2-3', 'Аксессуары')
    )
    name = models.CharField(max_length=225, blank=True, null=False, verbose_name='Halynyn ady',
                            help_text='Halynyn ady')
    name_ru = models.CharField(max_length=225, blank=True, null=False, verbose_name='Название кора',
                               help_text='Название ковра')
    name_en = models.CharField(max_length=225, blank=True, null=False, verbose_name='Carpet name',
                               help_text='Carpet name')

    description = models.CharField(max_length=500, blank=True, null=False, verbose_name='Haly barada maglumat',
                                   help_text='Haly barada gysgaca maglumat')
    description_ru = models.CharField(max_length=500, blank=True, null=False, verbose_name='Описание картины',
                                      help_text='Краткое описанние ковра')
    description_tm = models.CharField(max_length=500, blank=True, null=False, verbose_name='Description for carpet',
                                      help_text='Short description of carpet')

    size_of_carpet = models.CharField(max_length=255, blank=True, null=True, verbose_name='Размер ковара',
                                      help_text='4,5 m x 5 m')

    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    category = models.CharField(max_length=50, verbose_name='Категория картиины', blank=False, null=False,
                                choices=category_choice, default='Category 1')

    price = models.IntegerField(verbose_name='Стоисомть ковра', default=0)


class HomeBackgroundModel(models.Model):
    image = models.ImageField(upload_to='background/', verbose_name='Фото заднего фона')
    date = models.DateTimeField(auto_now_add=True)

    def image_to_admin(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    image_to_admin.short_description = 'Image'
    image_to_admin.allow_tags = True
