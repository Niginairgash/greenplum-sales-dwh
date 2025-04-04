Цель данного проекта создать dwh.

Описание проекта:
Этот pet-проект моделирует хранилище данных (DWH) c использованием Data Vault 2.0. Данные загружаются из CSV-файлов в Greenplum, затем агрегируются и анализируются.

📁 Структура проекта:
- data
    - categories.csv
    - products.csv
    - customers.csv
    - sales.csv
- sql
    
- scripts
    
README.md

📊 Data Vault 2.0 модель
Проект будет использовать Data Vault 2.0 для хранения и анализа данных
* Хаб-таблицы
* Линк-таблицы
* Сателлит-таблицы

🛠 Технологии
* Greenplum Database (MPP -хранилище)
* PostgreSQL (основа Greenplum)
* Docker (развертывание)
* Python (pandas, facker) (генерация данных)

Установка и запуск

Устанавливаем Docker : https://www.docker.com/get-started/
После в https://hub.docker.com/ находим образ apache/airflow 
или же в терминале пишем:
    docker pull apache/airflow
    