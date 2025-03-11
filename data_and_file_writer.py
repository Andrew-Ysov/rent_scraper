"""File with specifications for searching.

file_writer(data) writes all data (from VK and from site) in a single file.
"""

import csv

min_price = 8000
max_price = 25000
num_of_posts = 20
file_name = 'offers.csv'


def file_writer(data):
        with open(file_name, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(data)


if __name__ == '__main__':
        test_data = ''
        file_writer(test_data)