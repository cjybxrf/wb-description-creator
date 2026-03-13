from bs4 import BeautifulSoup

def my_parser(set_cards):

    str_cards = ''
    link = ''
    set_link = set()
    feedback = None
    set_feedback = set()
    link_and_feedback = dict()
    finally_links = list()


    for card in set_cards:
        str_cards += card

    soup = BeautifulSoup(str_cards, 'html.parser')
    
    product_card_wraper = soup.find_all('div', class_ = 'product-card__wrapper')

    for product in product_card_wraper:

        raw_link = product.find('a', class_ = 'product-card__link')
        if raw_link:
            link = raw_link.get('href')
        else:
            link = 'Нет ссылки'
        
        set_link.add(link)

        current_raw_feedback = product.find('span', class_ = 'product-card__count')
        if current_raw_feedback:
            current_feedback = ''
            raw_feedback = current_raw_feedback.get_text(strip = True)
            for i in raw_feedback:
                if i.isdigit():
                    current_feedback += i
            feedback = int(current_feedback)
            set_feedback.add(feedback)
        else:
            feedback = 0

        link_and_feedback[link] = feedback

    for _ in range(5):
        max_fb = max(set_feedback)
        set_feedback.remove(max_fb)

        for i in set_link:
            if link_and_feedback.get(i) == max_fb:
                finally_links.append(i)
                print(f'ПАРСИНГ----->{len(finally_links)}')
                break

    return finally_links