"""
Multi-Processing: ProcessPoolExecutor

ProcessPoolExecutor, as_completed

"""


import os
import urllib.request
import logging
from concurrent.futures import ProcessPoolExecutor, as_completed
from color import light_blue, yellow, reset, green


URLS = [
    'https://naver.com',
    'https://google.com',
    'https://reddit.com',
    'https://github.com'
]


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    parent_process_id = os.getpid()
    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}Start{reset}')

    with ProcessPoolExecutor(max_workers=4) as executor:
        # Future 로드(실행 X)
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}

        for future in as_completed(future_to_url):
            url = future_to_url[future]

            try:
                data = future.result()
            except Exception as e:
                print(f'{url} generated an exception: {e}')
            else:
                print(f'{light_blue}{url}{reset} page is {len(data)} bytes.')

    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}End{reset}')


if __name__ == '__main__':
    main()