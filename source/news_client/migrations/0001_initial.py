# Generated by Django 3.0 on 2020-12-13 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Категория')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_client.Category')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='Изображение')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='news_client.Category', verbose_name='Категория')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
