# Тестовое задание ISpring UI Tests.

## Подготовка проекта
- Установить Python 3.11:
https://www.python.org/downloads/

- Проверить версию Python:
```sh
python3 --version
```
- Перейти в директорию проекта
- Убедиться в наличии файла ```.env``` в корневой директории проекта. Пример:

```
BASE_URL=https://github.com/login
AUTH_LOGIN=test_user123123@gmail.com
AUTH_PASS=testpass123123!@#
```
   
- Установить зависимости:
```sh
pip install -U pip setuptools pipenv && pipenv install
 ```
- Установить веб-драйвер и необходимые библиотеки:
```sh
playwright install chromium
playwright install-deps
 ```


## Запуск тестов
Запуск тестов производится из директории проекта:
```sh
pytest --alluredir=allure_res ./tests -v -s
```
Для запуска с отображением окна браузера используйте тэг  `````--headed`````:
```sh
pytest --alluredir=allure_res ./tests -v -s --headed
```



## Запуск тестов с использованием Docker

- Установить Docker: https://docs.docker.com/engine/install/
- Установить docker-compose: https://docs.docker.com/compose/install/
- Убедиться, что включен docker daemon

Запуск тестов производится из директории проекта:
```sh
docker-compose up test_app
```
Для генерации отчета запустить команду:

```sh
docker-compose up -d allure
```

Открыть отчет можно по ссылке:
- http://localhost:5050/allure-docker-service/latest-report

