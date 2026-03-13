<div style='
width: 900px; 
border: dashed; 
display: flex; 
justify-content: center; 
align-items: center; 
padding-left: 15px;
padding-right: 11px; 
padding-top: 13px; 
margin-bottom: 25px;
border-radius: 7px;
background-color: #F5F5DC;'>
    <p style='font-size: 15px; color: #2D4031;'>
        <strong>Disclaimer:</strong> данный проект разработан исключительно в образовательных и демонстрационных целях как часть портфолио. Автор не несет ответственности за нецелевое использование скрипта или нарушение условий пользования сторонних ресурсов.
    </p>
</div>

<h1 style='border-bottom: none; color: #F2E9E4'>wb description creator</h1>

<h2>Описание</h2> 
<p style='font-size: 16px;'>
    Программа генерирует описание карточки товара, на основе взятых ключей у топ 5 карточек по количеству оценок покупателей. <br>Находит эти карточки по поисковому запросу пользователя и по выбранному городу. Сгенерированное описание выгружает в файл description.txt.
</p>

<h2>Стек</h2>
<ul>
    <li>Язык: Python 3.13.11</li>
    <li>Пользовательский интерфейс: Customtkinter</li>
    <li>Автоматизированный сбор данных с сайта: Playwright</li>
    <li>Парсинг собранной информации: BeautifulSoup</li>
    <li>Генерация описания: Yandex aliceai-llm</li>
    <li>Для идентификатора каталога и api ключа: dotenv</li>
    <li>Упаковка программы в один .exe файл: PyInstaller</li>
</ul>

<h2>Демонстрация программы</h2>
<p>
    <img src='assets/1_icon_exe.png' title='Иконка' style='border-radius: 5px;'>
</p>

<p>
    <img src='assets/2_gui.png' title='Интерфейс' style='border-radius: 5px;'>
</p>

<p>
    <img src='assets/3_example_of_work.png' title='Выполнение скрипта' style='border-radius: 5px;'>
</p>

<p>
    <img src='assets/4_description_example.png' title='Пример описания' style='border-radius: 5px;'>
</p>

<p>
    <img src='assets/5_text_parameters.png' title='Параметры сгенерированного текста' style='border-radius: 5px;'>
</p>

<h2>Установка</h2>
<div style='
width: 560px;
display: flex; 
justify-content: center; 
align-items: center;
background-color: #FFFFF0;
border-radius: 7px;
padding-top: 10px;
padding-left: 10px;
padding-right: 10px;
margin-bottom: 30px;'>
    <p style='font-size: 15px; color: #333333;'>
        <strong>Примечание:</strong> для работы программы вам понадобиться API ключ (API_KEY) и идентификатора каталога (FOLDER_ID). Получить их вы можете на сайте <a href='https://aistudio.yandex.ru/ru'>Яндекса</a>. После, их нужно вписать в соответствующие поля в файле <a href='.env.example'>.env</a>.
    </p>
</div>

<ol>
    <li>Клонируйте репозиторий любым удобным способом. Если у вас установлен git, скопируйте в консоль <code>https://github.com/cjybxrf/wb-description-creator.git</code></li>
    <li>Запустите скрипт установки <code>start build.cmd</code></li>
    <li>Заполните файл <code>.env</code></li>
    <li>Запустите завершающий скрипт установки <code>final build.cmd</code></li>
</ol>

<p>После установки файл DES_WB.exe будет лежать в папке dist. В процессе установки так же будут подсказки в консоли.</p>