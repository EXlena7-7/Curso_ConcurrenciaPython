import time
import requests
import threading
import logging
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
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

def check_status_code(response, url):
    logging.info(f'La respuesta del servidor {url} es: {response.status_code}')

def math_operation(n1,n2):
    return n1 + n2

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:

        results = executor.map(generate_request, URLS)

        for url, response in zip(URLS, results):
            if response.status_code == 200:
                check_status_code(response, url)