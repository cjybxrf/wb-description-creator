from playwright.sync_api import sync_playwright
import random

def my_scraper(query, city):

        #0 - Москва
        #1 - Санкт-Петербург
        #2 - Казань
        #3 - Самара
        #4 - Екатеринбург
        #5 - Владивосток

        geo = [
            {"latitude": 55.774246, "longitude": 37.631802}, 
            {"latitude": 59.873460, "longitude": 30.351182}, 
            {"latitude": 55.782568, "longitude": 49.137237}, 
            {"latitude": 53.197765, "longitude": 50.179205}, 
            {"latitude": 56.830634, "longitude": 60.628492}, 
            {"latitude": 43.122453, "longitude": 131.909953}
            ]
        
        geolocation_local = ''
        url = f'https://www.site_for_example.ru/catalog/0/search.aspx?search={query}'
        stop_request = False
        old_cards = 0
        count_to_exit = 0
        three_handred_cards = set()
        stop_limit = 300

        match city:
            case 'Москва':
                geolocation_local = geo[0]
            case 'Санкт-Петербург':
                geolocation_local = geo[1]
            case 'Казань':
                geolocation_local = geo[2]
            case 'Самара':
                geolocation_local = geo[3]
            case 'Екатеринбург':
                geolocation_local = geo[4]
            case 'Владивосток':
                geolocation_local = geo[5]


        with sync_playwright() as p:
            browser = p.chromium.launch(channel = 'chrome', headless = False, args = ['--disable-blink-features=AutomationControlled'])

            context = browser.new_context(no_viewport=True, permissions = ['geolocation'], geolocation = geolocation_local)

            page = context.new_page()

            page.goto(url)

            #ПАЗУА ДЛЯ ПРОГРУЗКИ СТРАНИЦЫ
            page.wait_for_timeout(random.randint(5672, 9939))
           
            #ВЫБОР ГОРОДА
            page.locator('.simple-menu__link--address').click(force = True)
            page.wait_for_timeout(random.randint(2569, 3039))
            page.get_by_text(city).nth(4).click(force = True)
            page.wait_for_timeout(random.randint(1044, 1539))
            page.get_by_role('button', name = 'Заберу отсюда').click()
            
            #ПАЗУА ДЛЯ ПРОГРУЗКИ СТРАНИЦЫ
            page.wait_for_timeout(random.randint(2672, 3939))

            try:
                while not stop_request:
                    #ОЖИДАНИЕ ЗАГРУЗКИ СЕЛЕКТОРА КОЛИЧЕСТВА ОЦЕНОК
                    page.wait_for_selector('.product-card__count')
                    
                    #СБОР ВСЕХ КАРТОЧЕК
                    raw_cards = page.locator('.product-card').all()
                    
                    #ДОБАВЛЕНИЕ УСЛОВНО УНИКАЛЬНЫХ КАРТОЧЕК
                    for card in raw_cards:
                        three_handred_cards.add(card.inner_html())

                    new_cards = len(three_handred_cards)
                    
                    #ИМИТАЦИЯ ДВИЖЕНИЯ КУРСОРА ПО ЭКРАНУ
                    page.mouse.move(random.randint(431, 542), random.randint(429, 553), steps=15)

                    #ИМИТАЦИЯ ПРОКРУТКИ КОЛЕСИКА
                    page.mouse.wheel(0, random.randint(691, 954))

                    #ПАЗУА ДЛЯ ПРОГРУЗКИ СТРАНИЦЫ
                    page.wait_for_timeout(random.randint(1072, 1739))

                    #ОСТАНОВКА ЦИКЛА ПО ДОСТИЖЕНИЮ 300 УСЛОВНО УНИКАЛЬНЫХ КАРТОЧЕК, ЛИБО КОНЦА СТРАНИЦЫ
                    if len(three_handred_cards) >= stop_limit:
                        browser.close()
                        stop_request = True
                    elif new_cards == old_cards:
                        count_to_exit += 1
                        print(f'ДО ВЫХОДА: {count_to_exit} ИЗ 4')
                        if count_to_exit == 4:
                            browser.close()
                            stop_request = True
                    else:
                        old_cards = new_cards
                        count_to_exit = 0

            except Exception as e:
                print(f'ПРИ ПОЛУЧЕНИИ КАРТОЧЕК ОШИБКА ТАКАЯ ---->{e}')
            finally:
                print(f'КАРТОЧЕК ВЗЯТО ---->{len(three_handred_cards)}')
                return three_handred_cards