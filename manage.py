import argparse


# Главная функция для запуска скрипта
def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser()
    # Добавляем аргументы
    parser.add_argument(
        "action",
        help="Action to perform",
        choices=["scaffoldDB"],
    )
    args = parser.parse_args()
    if args.action == "scaffoldDB":
        scaffoldDb()


# Функция для инициализации БД
def scaffoldDb():
    from database import scaffoldDb

    print("Scaffolding DB")
    scaffoldDb()
    print("DB Scaffolding complete")


if __name__ == "__main__":
    main()
