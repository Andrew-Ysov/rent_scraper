# файл для парсинга данных из vk

import requests
import json

from vk_api_token import vk_api_token
from data_and_file_writer import min_price, max_price, num_of_posts, file_writer


links = ['https://vk.com/arenda_lugansk1', 'https://vk.com/nedvizhimost_souz', 'https://vk.com/nedvizhimost_lnr1']

domains = [part.split('/')[-1] for part in links]


def is_valid_text(text:str):
        # для валидации текста нужно использовать регулярные выражения
        pass
        # text_list = text.lower().split()
        # unwanted_words = {'продажа','посуточная','продаётся','продам', 'сниму', 'снимет'}

        # for word in text_list:
        #         if word in unwanted_words:
        #                 return False
        # return True

def get_location(text:str):
        # для получения адреса нужно использовать регулярные выражения
        pass

def get_price(text:str):
        # для получения цены нужно использовать регулярные выражения
        pass
        # currency_pos = min(text.find('рублей'), text.find('руб'))
        # if currency_pos == -1:
        #         return ''

        # price_pos = currency_pos
        # while text[price_pos] and (text[price_pos].isdigit() or text[price_pos].isspace()):
        #         price_pos -= 1

        # price = text[price_pos:currency_pos+1]
        # return price

def get_link(json_data, domain, num):
        pass
        post_id = json_data['response']['items'][num]['id']
        owner_id = json_data['response']['items'][num]['from_id']
        return f'https://vk.com/{domain}?w=wall{owner_id}_{post_id}'

# def file_writer(data):
#         with open(file_name, 'a', newline='', encoding= 'utf-8') as file:
#                 writer = csv.writer(file)
#                 writer.writerow(data)

def post_parse():
        for domain in domains:
                count = num_of_posts
                r= requests.get('https://api.vk.com/method/wall.get',
                        params= {'domain':domain,
                                'count':count,
                                'access_token':vk_api_token,
                                'v':'5.199'})
                r.raise_for_status()

                json_data = json.loads(r.text)

                for num in range(count):
                        text = json.dumps(json_data['response']['items'][num]['text'], ensure_ascii=False)
                        if not text:
                                try: 
                                        text = json.dumps(json_data['response']['items'][num]['copy_history'][-1]['text'], ensure_ascii= False)
                                except:
                                        text = ''
                        price = ''
                        location = ''
                        # if is_valid_text(text):
                                # price = get_price(text)
                                # location = get_location(text)
                        
                        
                        link = get_link(json_data, domain, num)

                        file_writer([price, link])