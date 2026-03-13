from dotenv import load_dotenv
import os
import openai

def create_new_description_with_AI(descriptions, base_path):

    descriptions_str = ''

    for i in descriptions:
        descriptions_str += i

    load_dotenv(os.path.join(base_path, '.env'))
    YANDEX_CLOUD_API_KEY = os.getenv('YANDEX_CLOUD_API_KEY')
    YANDEX_CLOUD_FOLDER_ID = os.getenv('YANDEX_CLOUD_FOLDER_ID')
    YANDEX_CLOUD_MODEL = 'aliceai-llm'

    promt = f'Далее будет описания из карточек товаров с маркетплейса. Возьми ключевые слова из этих описаний и на их основе составь новое описание товара с использованием ключевых слов, но без упоминания брендов. Описание дожно быть не меннее 1600 символов и не более 1800 символов: {descriptions_str}'

    client = openai.OpenAI(
        api_key = YANDEX_CLOUD_API_KEY,
        project = YANDEX_CLOUD_FOLDER_ID,
        base_url = 'https://ai.api.cloud.yandex.net/v1'
    )

    response = client.responses.create(
        model = f'gpt://{YANDEX_CLOUD_FOLDER_ID}/{YANDEX_CLOUD_MODEL}',
        input = promt,
        temperature = 0.7,
        max_output_tokens = 800
    )

    with open('description.txt', 'w', encoding = 'utf-8') as f:
        f.write(response.output[0].content[0].text)

    print('ОПИСАНИЕ СОЗДАНО')