# YaCut - сервис укорачивания ссылок

### **Используемые языки, технологии**
Python3  
Flask  
Jinja2  
SQLAchemy  
Flask API  

##  **Описание проекта**
Сервис реализован на [Flask](https://flask.palletsprojects.com/en/2.2.x/), 
в качестве ORM используется SQLAchemy (модуль [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)). 
Для генерации HTML-страницы разработаны HTML-шаблоны (шаблонизатор Jinja2), 
для работы с формами применен модуль [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/).  
Также для проекта реализован API. Выполняется валидация данных и обработка ошибок. 

**Ключевые возможности:**
- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.

**Пример POST-запроса к API-проекта и успешного ответа:**

POST-запрос к эндпоинту http://127.0.0.1:5000/api/id/  
Request
```
{
    "url": "https://flask-restful.readthedocs.io/en/latest/",
    "custom_id": "flasklatest"
}
```
Response
```
{
    "short_link": "http://127.0.0.1:5000/flasklatest",
    "url": "https://flask-restful.readthedocs.io/en/latest/"
}
```

## **Запуск проекта**
Выполните следующие команды в терминале.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
4.  Создать файл «.env», добавив в него переменные окружения:
```
touch .env
```
5. Выполнить команду запуска проекта:
```
flask run
```
### _Описание шаблона .env_
Необходимо указать переменные окружения в следующем формате:

FLASK_APP = *название приложения*  
FLASK_ENV = *режим работы приложения: продакшен или разработка*    
DATABASE_URI = *подключение БД, например: sqlite:///db.sqlite3*   
SECRET_KEY = *уникальный секретный ключ*  


## **Работа со спецификацией**
Для работы с документацией файл ```openapi.yml``` можно открыть 
в онлайн-редакторе [Swagger Editor](https://editor.swagger.io). 

## **Тестирование через HHTP-клиент**
Для тестирования работы API проекта удобно пользоваться 
HHTP-клиентами: [Postman](https://www.postman.com) или [httpie](https://httpie.io). 


## Авторы: Павел Сердюков ([PavelPrist](https://github.com/PavelPrist/)), ЯндексПрактикум