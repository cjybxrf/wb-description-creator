from playwright.sync_api import sync_playwright
import random

def get_description(parsed_cards):
     
    descriptions = list()

    with sync_playwright() as p:

        browser = p.chromium.launch(channel = 'chrome', headless = False, args = ['--disable-blink-features=AutomationControlled'])

        context = browser.new_context(no_viewport=True)

        page = context.new_page()

        for i in range(len(parsed_cards)):
            page.goto(parsed_cards[i])

            page.wait_for_timeout(random.randint(5672, 6939))

            page.locator('.btnDetailText--nrkiv').scroll_into_view_if_needed()
            page.locator('.btnDetailText--nrkiv').click()

            try:
                page.wait_for_timeout(random.randint(3672, 4939))
                page.locator('.descriptionText--Jq9n2').scroll_into_view_if_needed()
                des_text = page.locator('.descriptionText--Jq9n2')
                descriptions.append(des_text.inner_text())
            except Exception as e:
                print(f'ПРИ ПОЛУЧЕНИИ ОПИСАНИЯ ОШИБКА ТАКАЯ ----->{e}')
                continue

        browser.close()

    return descriptions