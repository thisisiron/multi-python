"""
Threading 2: Daemon

Daemon Thread
    1. Main-Thread 종료시 즉시 종료 
    (DON'T FORGET! Sub-Thread는 Main-Thread가 종료되더라도 자신의 일이 끝나지 않으면 계속 수행)
    2. 주로 Backgound 무한 대기 이벤트 발생 실행하는 곳에 사용

※ 주의
    상황: Daemon을 True로 설정하고 굳이 join함수를 사용한 경우 
    -> 끝까지 다 실행하고 종료, Daemon을 설정한 의미가 없어짐
"""


import logging
import threading

from color import light_blue, yellow, reset, green, red


def run_thread(id, r):
    logging.info(f'{light_blue}[Sub-{id}] {yellow}Start{reset}')

    for i in r:
        logging.info(f'{light_blue}[Sub-{id}] {yellow}{i}{reset}')

    logging.info(f'{light_blue}[Sub-{id}] {yellow}End{reset}')


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info(f'{green}[Main] {yellow}Start{reset}')

    # x = threading.Thread(target=run_thread, args=('0', range(456)))
    # y = threading.Thread(target=run_thread, args=('1', range(456)))

    # Daemon default 값은 False
    x = threading.Thread(target=run_thread, args=('1', range(456)), daemon=True)
    y = threading.Thread(target=run_thread, args=('2', range(456)), daemon=True)

    logging.info(f'{red}is x Daemon? {x.isDaemon()}{reset}')

    # Start Sub-Thread
    x.start()
    y.start()

    # Check the two lines below
    # x.join()
    # y.join()

    logging.info(f'{green}[Main] {yellow}Wait for sub-thread{reset}')

    logging.info(f'{green}[Main] {yellow}End{reset}')


if __name__ == '__main__':
    main()