1. Проініціалізував середовище pipenv та встановив необхідні пакети
2. Створив pipenv run django-admin startproject my_site && mv my_site/my_site/* my_site/ && mv my_site/manage.py ./
3. Запуститв сервер. Використовуючи команду [pipenv run python manage.py runserver] та переходжу за посиланням яке вивелось у консолі:
 ![alttext](https://github.com/Prometej007/devops_course-labs/blob/master/lab3/source/start.png)
4. Зупинив сервер 
5. Створив темплейт додатку
6. Додав файл з розширенням .html та main/urls.py
7. Вказую Django frameworks назву створеного додатку та де шукати веб сторінки. Це здійснюється у файлі web_site/settings.pyу у змінній INSTALLED_APPS, а також вношу зміни у файл web_site/url.py.
8. Змінюю вміст файла main/views.py
9. Заповнюю файл main/urls.py згідно зразка.
10. Запускаю сервер та переконуюсь що сторінки доступні:
 ![alttext](https://github.com/Prometej007/devops_course-labs/blob/master/lab3/source/tempalte.png)
11. Встановив бібліотеку requests
12. Модифікую функцію health 
 ![alttext](https://github.com/Prometej007/devops_course-labs/blob/master/lab3/source/health.png)
13. Дописую функціонал який буде виводити повідомлення про недоступність сайту.
14. Переробляю monitoring.py так щоб дана програма запускалась раз в хвилину.
15. add server log
