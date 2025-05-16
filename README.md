## Инструкция по развертыванию проекта
1. Создать виртуальное окружение
```
python3 -m venv todos_venv
```
2. Активировать виртуальное окружение
```
source todos_venv/bin/activate
```
3. Установить нужные библиотеки
```
python -m pip install -r requirements.txt
```
4. Применить миграции
```
alembic upgrade head
```

5. Запустить приложение
```
python main.py
```

### Как создать миграцию
```
alembic revision --autogenerate -m "Initial migration"
```