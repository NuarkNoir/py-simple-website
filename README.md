### py-simple-website

---

> Note: данный пример был создан на `Python 3.10.7`

### Как запустить

##### 1. Создаём виртуальное окружение

```sh
python -m venv venv
```

##### 2. Активируем виртуальное окружение

Linux: 
```sh
source venv/bin/activate
```

Windows (w/ Powershell):
```powershell
venv/Scripts/activate.ps1
```

##### 3. Устанавливаем библиотеки

```sh
pip install -r requirements.txt
```

##### 4. Настраиваем приложение

В файле `config.py` меняем конфиг, на соответствующий вашему:
```python
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "admin"
DB_NAME = "db"
```

##### 5. Инициализируем базу данных

> Note: база данных `DB_NAME` будет дропнута! Если там есть важные данные, выберите имя другой, не существующей базы

```sh
python manage.py scaffoldDB
```

##### 6. Запускаем приложение

```sh
hypercorn app:app
```
