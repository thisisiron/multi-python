"""
Threading 3: ThreadPoolExecutor, submit

job1: 0부터 100까지 합
job2: 0부터 1000까지 합

concurrent module 사용
    1. Threading을 하나 하나 생성해서 사용하는 것이 아니라 여러 Thread를 생성하여 사용
    2. 간편하게 with를 사용하여 Thread 생성 및 소멸(Lifecycle 관리 용이)  -> 3-2에서 사용
    3. 디버깅 어려움(단점)
"""


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

    # max_workers: 
    executor = ThreadPoolExecutor(max_workers=3)

    job1 = executor.submit(do, '1', range(101))
    job2 = executor.submit(do, '2', range(1001))

    logging.info(f'{green}[Main] {yellow}Sub-1 Result -> {job1.result()}{reset}')
    logging.info(f'{green}[Main] {yellow}Sub-2 Result -> {job2.result()}{reset}')

    logging.info(f'{green}[Main] {yellow}End{reset}')


if __name__ == '__main__':
    main()