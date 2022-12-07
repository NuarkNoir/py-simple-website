from mysql.connector import connect, Error
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


# Функция для создания базы данных
def scaffoldDb():
    try:
        # Подключаемся к базе данных
        with connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWORD,
        ) as connection:
            # Создаем курсор
            with connection.cursor() as cursor:
                print(f"Dropping and creating database '{DB_NAME}'")
                # Удаляем базу данных, если она существует
                cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")
                # Создаем базу данных
                cursor.execute(f"CREATE DATABASE {DB_NAME}")
                print(f"Database '{DB_NAME}' created")
                print("Creating tables")
                # Выбираем базу данных
                connection.database = DB_NAME
                # Запрос создания таблицы для форм
                create_tables_query = """
                CREATE TABLE IF NOT EXISTS forms (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    email VARCHAR(255) NOT NULL,
                    title VARCHAR(255) NOT NULL,
                    text VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
                # Выполняем запрос
                cursor.execute(create_tables_query)
                print("Tables created")
    except Error as e:
        print(e)
        exit(1)


# Функция для создания подключения к базе данных
def create_connection():
    connection = None
    try:
        connection = connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWORD,
            database=DB_NAME,
        )
    except Error as e:
        print(f"The error '{e}' occurred")
        exit(1)

    return connection


# Функция для получения всех форм
def get_forms():
    try:
        # Создаем подключение и курсор
        # После выполнения блока with подключение и курсор закроются автоматически
        with create_connection() as connection, connection.cursor() as cursor:
            cursor.execute("SELECT * FROM forms")
            forms = cursor.fetchall()
            return forms, None
    except Error as e:
        print(e)
        return None, e


# Функция для создания формы
def create_form(email: str, title: str, text: str):
    try:
        # Создаем подключение и курсор
        with create_connection() as connection, connection.cursor() as cursor:
            # Запрос на создание формы, вместо %s будут подставлены переменные
            cursor.execute(
                "INSERT INTO forms (email, title, text) VALUES (%s, %s, %s)",
                (email, title, text),
            )
            connection.commit()
    except Error as e:
        print(e)
        return e

    return None


# Функция для удаления формы
def delete_form(id: int):
    try:
        # Создаем подключение и курсор
        with create_connection() as connection, connection.cursor() as cursor:
            # Запрос на удаление формы, вместо %s будет подставлен id
            cursor.execute("DELETE FROM forms WHERE id=%s", (id,))
            connection.commit()
    except Error as e:
        print(e)
        return e

    return None
