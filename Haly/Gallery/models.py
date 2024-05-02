from django.db import models
from django.utils.safestring import mark_safe
from django.shortcuts import redirect


class GalleryModel(models.Model):
    category_choice = (
        ('Category 1', 'Большие ковры'),
        ('Category 2', 'Изделия из ковров'),
        ('Category 3', 'Аксессуары')
    )
    name = models.CharField(max_length=225, blank=True, null=False, verbose_name='Halynyn ady',
                            help_text='Halynyn ady')
    description = models.CharField(max_length=500, blank=True, null=False, verbose_name='Haly barada maglumat',
                                   help_text='Haly barada gysgaca maglumat')
    size_of_carpet = models.CharField(max_length=255, blank=True, null=True, verbose_name='Haly razmery',
                                      help_text='4,5 m x 5 m')
    image = models.ImageField(upload_to='gallery/', verbose_name='Surat')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Doredilen senesi')
    category = models.CharField(max_length=50, verbose_name='Haly kategoriyasy', blank=False, null=False,
                                choices=category_choice, default='Category 1')
    price = models.IntegerField(verbose_name='Bahasy', default=0)

    def save(self, *args, **kwargs):
        self.image.name = f'{self.category}/{self.image.name}'
        return super().save(*args, **kwargs)

    def image_to_admin(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    image_to_admin.short_description = 'Image'
    image_to_admin.allow_tags = True

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Haly'
        verbose_name_plural = 'Halylar'


class GalleryHomeModel(models.Model):
    category_choice = (
        ('tabs-2-1', 'Большие ковры'),
        ('tabs-2-2', 'Изделия из ковров'),
        ('tabs-2-3', 'Аксессуары')
    )
    name = models.CharField(max_length=225, blank=True, null=False, verbose_name='Halynyn ady',
                            help_text='Halynyn ady')
    description = models.CharField(max_length=500, blank=True, null=False, verbose_name='Haly barada maglumat',
                                   help_text='Haly barada gysgaca maglumat')
    size_of_carpet = models.CharField(max_length=255, blank=True, null=True, verbose_name='Haly razmery',
                                      help_text='4,5 m x 5 m')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Doredilen senesi')
    category = models.CharField(max_length=50, verbose_name='Haly kategoriyasy', blank=False, null=False,
                                choices=category_choice, default='Category 1')
    price = models.IntegerField(verbose_name='Bahasy', default=0)

    def save(self, *args, **kwargs):
        if self.__class__.objects.filter(category=self.category).count() >= 3:
            return
            # raise ValidationError(f"Dine 3 haly bir kategoriya birikdirip bolyar {self.category}")
        return super().save(*args, *kwargs)

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = 'Haly bahalar'
        verbose_name_plural = 'Haly bahalary'


class HomeBackgroundModel(models.Model):
    image = models.ImageField(upload_to='background/', verbose_name='Arka fon')
    date = models.DateTimeField(auto_now_add=True)

    def image_to_admin(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    image_to_admin.short_description = 'Image'
    image_to_admin.allow_tags = True

    class Meta:
        verbose_name = 'Arka fon'
        verbose_name_plural = 'Arka fon'
