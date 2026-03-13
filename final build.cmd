@echo off

color FA

echo [1/1] Создание DES_WB.exe файла

echo.

call venv\Scripts\activate
pyinstaller --onefile --icon=app_icon.ico --name=DES_WB --add-data "app_icon.ico;." --add-data ".env;." gui.py

echo. 

echo Готово! Все установлено. Файл запуска программы DES_WB.exe лежит в папке dist. 
echo Все остальное можно удалить. Эти файлы нужны для сборки и на работу никак не влияют.

echo. 

echo Нажмите любую кнопку для закрытия окна

pause