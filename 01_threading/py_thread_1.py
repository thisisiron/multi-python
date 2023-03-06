"""
Threading 1: Threading 사용 방법과 Join 함수

Sub-Thread는 Main-Thread 종료 여부와 상관없이 자신의 코드를 끝까지 수행하고 끝남
하지만 Join 함수를 통해서 Sub-Thread가 종료될 때까지 Main-Thread를 Stop (Daemon Thread 방법도 존재)
"""


import time
import logging
import threading

from color import light_blue, yellow, reset, green


def run_thread(id):
    logging.info(f'{light_blue}[Sub-{id}] {yellow}Start{reset}')
    time.sleep(3)
    logging.info(f'{light_blue}[Sub-{id}] {yellow}End{reset}')


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info(f'{green}[Main] {yellow}Start{reset}')

    x = threading.Thread(target=run_thread, args=('1',))

    # Start Sub-Thread
    x.start()

    # Check the line below
    x.join()

    logging.info(f'{green}[Main] {yellow}Wait for sub-thread{reset}')

    logging.info(f'{green}[Main] {yellow}End{reset}')


if __name__ == '__main__':
    main()