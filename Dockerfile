# Используем образ Python для Django
FROM python:3.12

# Устанавливаем переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app


# Копируем проект в рабочую директорию контейнера
COPY ./khnz /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Собираем статические файлы Django
RUN python manage.py collectstatic --noinput

# Определяем порт, который будет использоваться при запуске контейнера
EXPOSE 8000

# Команда для запуска Django приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

