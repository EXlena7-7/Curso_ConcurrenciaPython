import time
import requests
import threading
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

URLS = [
    'https://twitter.com/home',
    'https://randomuser.me/api',
    'https://www.google.com',
    'https://es.stackoverflow.com',
    'https://about.gitlab.com',
    'https://github.com',
    'https://www.youtube.com/'
]

def generate_request(url):
    return requests.get(url), url # Tuple

def check_status_code(response):
    logging.info(f'La respuesta del servidor {response[1]} es: {response[0].status_code}')

def math_operation(n1,n2):
    return n1 + n2

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        futuros = [ executor.submit(generate_request, url) for url in URLS ]

        for futuro in futuros:
            futuro.add_done_callback(
                lambda future: check_status_code(future.result())
        )