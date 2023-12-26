# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /web_miet
# Копирует все файлы из нашего локального проекта в контейнер
ADD ./ ./
COPY requirements.txt /tmp/requirements.txt
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
EXPOSE 8000
RUN python3 -m pip install -r /tmp/requirements.txt

