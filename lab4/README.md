1.Тестування чи встановленний докер та переврка версії за допомогою команд та перенаправив вивід у файл docker.log
 docker -v
 docker -h
 
2.Створюю імедж із Django зробленим у попередній роботі.

  [docker pull python:3.7-slim]
  
  [docker images]
  
  [docker inspect python:3.7-slim]
  
За базу необіхдно взяти основу на python  

2.1 Створюю файл з іменем Dockerfile, копіюю туди вміст такого ж файлу з репозиторію devops_course;
2.2 Ознайомлююсь із коментарями та структурою написання Dockerfile;

3.Створюю власний репозиторій на Docker Hub.Назва аккаунту - [prometej46297] У вкладці Repositories -> кнопку Create new repository. Називаю його lab_4

4.Роблю білд імеджа та завантажую його до репозиторію. Для цього вказую правильну назву репозиторію та TAG.

  [docker build -t prometej46297/lab_4:latest - < Dockerfile]
  
  [docker images]
  
  [docker push prometej46297/lab_4:latest]

====[Посилання на Docker Hub репозиторій;](https://hub.docker.com/repository/docker/prometej46297/lab_4)=====

5. Для запуску веб-сайту потрібно виконати команду:
    docker run -it --name=lab_4 --rm -p 8000:8000 prometej46297/lab_4:latest
    

6.Виконую ті самі дії для створення репозиторію з моніторингом та паралельно з сайтом.

7. Зробив та запустив контейнер з моніторингом та перенаправив логи у server.log 
