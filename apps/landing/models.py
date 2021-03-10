from django.db import models

from singleton_model import SingletonModel


class Logo(models.Model):
    logo = models.ImageField(verbose_name='Логотип', upload_to='logos')

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'

    def __str__(self):
        return f'{self.logo}'


class Content(SingletonModel):
    title = models.CharField(verbose_name='Заголовок', max_length=32)
    description = models.TextField(verbose_name='Описание', max_length=128)
    logo = models.ForeignKey(Logo, on_delete=models.SET_NULL, null=True,
                             blank=True, verbose_name='Логотип',)

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'

    def __str__(self):
        return f'{self.title}'


class AboutUs(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=32)
    sub_title = models.CharField(verbose_name='Подзаголовок', max_length=32)
    description = models.TextField(verbose_name='Описание', max_length=128)
    video = models.FileField(verbose_name='Видео', upload_to='about_us_videos')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return f'{self.title}'


class AboutUsImage(models.Model):
    image = models.ImageField(verbose_name='Фотография', upload_to='about_us_images')
    about_us_id = models.ForeignKey(AboutUs, blank=True, null=True,
                                    verbose_name='О нас', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Фотография о нас'
        verbose_name_plural = 'Фотографии о нас'

