# Тестовое задание
# Административная панель для новостного клиента.
stack: Python 3.6, Django 3.0, DRF 3.12 Bootstrap4.

*Личные данные БД, секретный ключ, режим DEBUG (отладка) и локальные настройки вынесены в переменные окружения (они не должны попадать в публичные репозитории!!!) 
Для облегчения проверки, в данном задании использовалась MySQL, в связи с чем, переменные конфигурации БД (SQL_ENGINE, SQL_HOST, SQL_PORT, SQL_USER, SQL_PASSWORD...) указывать не нужно.
SECRET_KEY приложеня указан в примере конфигурации .env-файла, это было сделано так же, для облегчения проверки проекта. (Ни в коем случае, не оставляйте в публичном доступе секретные ключи и личные конфигурации.)
За дополнительной информацией по ИБ(информационной безопасности) в [google.com](https://www.google.com/):)!!!*

## Start
1) Склонируйте проект
Клонировать: **git clone  https://github.com/big-arturka/test_task**  
2) Перейдите в каталог склонированного проекта, создайте и активируйте виртуальное окружение:   
Создать: **python3 -m virtualenv -p python3 venv**  
Активировать: **. venv/bin/activate**

3) Создайте .env-файл с переменными окружения и заполните по примеру, указанному ниже:

DEBUG={РЕЖИМ ОТЛАДКИ} True or False       
SECRET_KEY={СЕКРЕТНЫЙ КЛЮЧ ПРИЛОЖЕНИЯ} ( "bz%4@2xw3=+#@x7*birr9d@9dl)(-j0ii#4-dff564##-3j*d(" - секретный ключ данного приложения )      
DJANGO_ALLOWED_HOSTS={СПИСОК РЗРЕШЕННЫХ ХОСТОВ/ДОМЕНОВ}     

4) Установите все зависимости в виртуальное окружение:   
**pip install -r requirements.txt**
(Примечание, нижеприведенные команды (./manage.py) доступны только из корнегого каталога проекта Django, где находятся все модули и конфигурационные файлы. В данном проекте, это папка "source". )
5) Перейдите в корневую директорию самого проекта (source) и проведите миграции:   
**./manage.py migrate**
6) Распакуйте приложенный к проекту архив uploads (изображения для тестовых статей) в корневой каталог (source)
7) Восстановите фикстуры (json-файлы содержащие перечень тестовых данных, для проверки проекта) командой:     
**./manage.py loaddata fixtures/auth.json fixtures/dump.json**

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
Доступ к приложению имеют только авторизованные Пользователи.
Администратор данного приложения имеет все привелегии, кроме смены пароля сторонним Пользователям.
Создать стороннего пользователя в административной панели может, только сам Администратор, далее пользователь может зайти на сайт, 
сменить пароль и отредактировать личные данные.

Сторонние пользователи могут исключительно просматривать Статьи, Категории, списки пользователей и личную страницу Пользователя.


## accounts
Приложение имеет представления для создания пользователя, просмотра личной страницы, редактирования данных, смены пароля и удаления пользователя.
Сторонним пользователям, выданы разрешения на: редактирование личной страницы, смену своего пароля, просмотра любых статей, категорий и других пользователей без права редактирования.


## news_client
Имеет в себе модели статей и категорий.
Представления осуществляющие действия CRUD для вышеупомянутых моделей.
Действие удаление, реализовано с подтверждением, для исключения случайных удалений данных.


## API
Приложение предоставляет открытое API и 2 точки входа, по которым можно получить данные о статьях и комментариях, в формате JSON.
Все пользователи, включая неавторизованных, могут получить данные о статьях и категориях, обращаясь к точкам доступа:

Для получения списка статей и их данных:
[http://localhost:8000/api/v1/articles/](http://localhost:8000/api/v1/articles/)

Для получения списка категорий:
[http://localhost:8000/api/v1/categories/](http://localhost:8000/api/v1/categories/)


## Тесты
На все представления данного приложения напсаны модульные тесты, проверяющие работоспособность, имитирующие авторизованные и анонимные запросы.
В представления создания и редактирования, полученные данные сверяются с тестовыми.
Для того, чтобы запустить тестирование, выполните:  
**./manage.py test**


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
 напишите на электронную почту <arturkrmnlv10@gmail.com>.
 
 
