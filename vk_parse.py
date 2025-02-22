"""Parsing posts from VK

post_parse(): parses number of posts from VK groups.
number of posts is set beforehand in data_and_file_writer.py
"""

import requests
import json

from vk_api_token import vk_api_token
from data_and_file_writer import min_price, max_price, num_of_posts, file_writer


links = ['https://vk.com/arenda_lugansk1', 'https://vk.com/nedvizhimost_souz', 'https://vk.com/nedvizhimost_lnr1']
domains = [part.split('/')[-1] for part in links]

# TODO: make text processing functions with regex


def get_link(json_data, domain, num):
        """Get a link to a specific post in VK."""
        post_id = json_data['response']['items'][num]['id']
        owner_id = json_data['response']['items'][num]['from_id']
        return f'https://vk.com/{domain}?w=wall{owner_id}_{post_id}'


def post_parse():
        """Parsing, processing and saving count of posts."""
        count = num_of_posts
        for domain in domains:
                r = requests.get('https://api.vk.com/method/wall.get',
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
                                        text = json.dumps(json_data['response']['items'][num]
                                                          ['copy_history'][-1]['text'], ensure_ascii=False)
                                except:
                                        text = ''
                        price = ''
                        link = get_link(json_data, domain, num)

                        file_writer([price, link])


if __name__ == '__main__':
        post_parse()