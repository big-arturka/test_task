# Тестовое задание
# Административная панель для мобильного новостного клиента.
stack: Python3.6, Django3.0

## Start
1) Склонируйте проект
2) Распакуйте приложенный к проекту архив uploads в то же самое место (изображения для тестовых статей)
3) Восстановите фикстуры из корневой папки проекта (sourse) командой: ./manage.py loaddata fixtures/auth.json fixtures/dump.json

В фикстурах содержаться тестовые данные:

1) accounts:

Administrator:
- username: admin
- password: admin

Other user:
- username: user
- password: user

2) news_client

Articles
- Title: What is a Programmer?
- Title: System administration

Categories
- IT-Technology - parrent: None
- System administration - parrent: IT-Technology

Приложение позволяет управлять (просматривать, добавлять, редактировать и удалять) всеми имеющимеся сущностями, в частности: Статьями, Категориями, Пользователями.
Доступ на страницу административной панели имеют только авторизованные Пользователи.
Администратор данной панели имеет все привелегии, кроме смены пароля сторонним Пользователям.
Создать стороннего пользователя в административной панели может, только сам Администратор, далее пользователь может зайти на сайт, 
сменить пароль и отредактировать личные данные.

Сторонние пользователи могут исключительно просматривать Статьи, Категории, списки пользователей и личную страницу Пользователя.


## accounts
Приложение имеет представления для создания пользователя, просмотра личной страницы, редактирования данных, смены пароля и удаления пользователя.
Сторонним пользователям, выданы разрешения на: редактирование личной страницы, смену пароля,просмотра статей, категорий и других пользователей без права редактирования.


## news_client
Имеет в себе модели статей и категорий.
Представления осуществляющие действия CRUD для вышеупомянутых моделей.
Действие удаление, реализовано с подтверждением, для исключения случайных удалений данных.


## API
Приложение предоставляет открытое API и 2 точки входа, по которым можно получить данные о статьях и комментариях, в формате JSON.
Все пользователи, включая неавторизованных, могут получить данные о статьях и категориях, обращаясь к точкам доступа:

Для получения списка статей и их данных:
[http://localhost:8000/api/v1/articles/] 

Для получения списка категорий:
[http://localhost:8000/api/v1/categories/]


## Тесты
На все представления данного приложения напсаны модульные тесты, проверяющие работоспособность иметирующие авторизованные и анонимные запросы.
В представления создания и редактирования, полученные данные сверяются с тестовыми.
Для того, чтобы запустить тестирование, выполните из корневой папки (source) проекта команду:  
./manage.py test


## Зависимости
- Django==3.0 (Веб-фреймворк Python.)
- pytz==2020.4 (Переносит базу данных Olson tz в Python. Эта библиотека позволяет выполнять точные и кросс-платформенные вычисления часовых поясов с использованием Python.)
- asgiref==3.3.1 (Содержит различные эталонные реализации ASGI.)
- sqlparse==0.4.1 (Обеспечивает поддержку синтаксического анализа, разделения и форматирования операторов SQL.)
- django-widget-tweaks==1.4.8 (Для настройки отображения полей формы в шаблонах. Поддерживается изменение классов CSS и атрибутов HTML.)
- djangorestframework==3.12.1 (REST-api фреймворк, использовался для написания представлений на основе представления DRF APIView и сериализации данных для отправке при обращении к энд-поинтам.)
- Pillow==7.2.0 (Библиотека изображений Python, добавляет возможности обработки изображений и работы с ними.)

## Поддержка

Если у вас возникли сложности или вопросы по использованию приложения,  
 напишите на электронную почту <example@example.com>.
 
 
