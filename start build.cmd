@echo off

color 3F

echo [1/3] Создание виртуального окружения (папка venv)
python -m venv venv
call venv\Scripts\activate

echo.

echo [2/3] Обновление pip и установка зависимостей

echo.

python -m pip install --upgrade pip
pip install -r requirements.txt

echo.

echo [3/3] Изменение имени файла .env.example на .env

echo.

ren .env.example .env

echo Теперь заполните файл .env вашими YANDEX_CLOUD_API_KEY и YANDEX_CLOUD_FOLDER_ID.
echo После заполнения запустите "final build" для сборки проекта.

echo.

echo Нажмите любую кнопку для закрытия окна

pause