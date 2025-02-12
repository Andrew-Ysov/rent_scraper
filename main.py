from ligakvartir_lug_parser import site_parse
from vk_parse import post_parse
from data_and_file_writer import site_link

if __name__ == '__main__':
    site_parse(site_link)
    post_parse()