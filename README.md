# DRF_homework_24.1 Вьюсеты и дженерики.

* Задание 1
Создайте новый Django-проект, подключите DRF в настройках проекта.

* Задание 2
Создайте следующие модели:

Пользователь:
- все поля от обычного пользователя, но авторизацию заменить на email;
- телефон;
- город;
- аватарка.  
Модель пользователя разместите в приложении users

Курс:
- название,
- превью (картинка),
- описание.

Урок:
- название,
- описание,
- превью (картинка),
- ссылка на видео.

* Задание 3  
Опишите CRUD для моделей курса и урока. Для реализации CRUD для курса используйте Viewsets, а для урока - Generic-классы.

Для работы контроллеров опишите простейшие сериализаторы.