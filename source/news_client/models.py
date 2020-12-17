from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Category')
    parent_id = models.ForeignKey('self', null=True, blank=True,
                                  verbose_name='Parent category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    category_id = models.ForeignKey('news_client.Category', on_delete=models.CASCADE,
                                    related_name='articles', verbose_name='Category')
    user_id = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_DEFAULT, default=1,
                                related_name='articles', verbose_name='Author')
    title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField(max_length=3000, verbose_name='Description')
    image = models.ImageField(null=True, blank=True, upload_to='pictures', verbose_name='Image')

    def __str__(self):
        return f'{self.pk}-{self.title}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
