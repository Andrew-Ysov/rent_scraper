# файл, хранящий требования к предложениям аренды и работающий с файлом результатов

import csv

min_price = 8000
max_price = 25000
num_of_posts = 20
site_link = 'https://www.ligakvartir.ru/lugansk/snyat-nedvizhimost'
file_name = 'offers.csv'


def file_writer(data):
        with open(file_name, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(data)


if __name__ == '__main__':
        pass