"""
Threading 3: ThreadPoolExecutor, map

map 함수: order를 보장

ThreadPoolExecutor을 with로 이용하여 실행
    max_workers를 적절히 설정
"""


import time
import logging
from concurrent.futures import ThreadPoolExecutor
from color import light_blue, yellow, reset, green


def do(id, r):
    logging.info(f'{light_blue}[Sub-{id}] {yellow}Start{reset}')

    total = 0
    for i in r:
        total += i

    logging.info(f'{light_blue}[Sub-{id}] {yellow}End, Result: {total}{reset}')
    return total


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info(f'{green}[Main] {yellow}Start{reset}')

    ts = time.time()
    with ThreadPoolExecutor(max_workers=3) as executor:
        jobs = executor.map(do, ['1', '2', '3', '4'], [range(10000001), range(1000001), range(100001), range(10001)])
        logging.info(f'{green}[Main] {yellow}Result of jobs -> {list(jobs)}{reset}')
    print(f'{time.time() - ts} sec')

    logging.info(f'{green}[Main] {yellow}End{reset}')


if __name__ == '__main__':
    main()