# avito_trainee
Цель задания – Необходимо создать сервис для хранения и подачи объявлений. Объявления должны храниться в базе данных. Сервис должен предоставлять API, работающее поверх HTTP в формате JSON.

Требования
язык, технологии: Python, PostgreSQL, Django REST framework
код должен быть выложен на github
3 метода: получение списка объявлений, получение одного объявления, создание объявления
валидация полей (не больше 3 ссылок на фото, описание не больше 1000 символов, название не больше 200 символов)

Методы:
Методы обрабатывают HTTP POST/GET запросы c телом, содержащим все необходимые параметры в JSON.

Получение списка объявлений
Запрос
http://localhost:8000/api/get_list/
GET-Аргументы: page, sort_date(asc/desc), sort_price(asc/desc)
Ответ: список объявлений (название объявления, ссылка на главное фото (первое в списке), цена)

Получение конкретного объявления
Запрос
http://localhost:8000/api/get_list/1
GET-аргументы: fields
Ответ: название объявления, цена, ссылка на главное фото(опционально: описание, ссылки на все фото)

Создание объявления
Запрос
request POST \ 
'{title: "title", 
description: "description", 
photos: ['https://hello.jpg',
         'https://hello.jpg'],
price:1}'
http://localhost:8000/api/create/
Ответ: id объявления, код результата
