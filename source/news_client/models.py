from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Категория')
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}-{self.parent_id}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    category_id = models.ForeignKey('news_client.Category', on_delete=models.CASCADE,
                                    related_name='articles', verbose_name='Категория')
    user_id = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_DEFAULT, default=1,
                                related_name='articles', verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, upload_to='pictures', verbose_name='Изображение')

    def __str__(self):
        return f'{self.pk}-{self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
