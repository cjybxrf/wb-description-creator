from my_scraper import my_scraper
from my_parser import my_parser
from get_description import get_description
from create_new_description_with_AI import create_new_description_with_AI

def center(query, city, base_path):
    cards = my_scraper(query, city)
    parsed_cards = my_parser(cards)
    descriptions = get_description(parsed_cards)
    create_new_description_with_AI(descriptions, base_path)