"""
Threading 5: Queue

Producer / Consumer Pattern

5-1에서 무한 실행되는 문제 해결 방법:
    With문 안에 set 함수 호출
"""


import time
import threading
import queue
import logging
import random
from concurrent.futures import ThreadPoolExecutor
from color import light_blue, yellow, reset, green, bold_red


def producer(queue, event):
    """ 네트워크 대기 상태 (서버)"""
    while not event.is_set():  # init 값은 0이므로 실행, event.set()이 호출되면 1이 되기 때문에 실행되지 않음
        msg = random.randint(1, 11)
        queue.put(msg) 
        logging.info(f'{light_blue}[Producer] {yellow}got msg -> {msg}{reset}')

    logging.info(f'{light_blue}[Producer] {yellow}received event{reset}')


def consumer(queue, event):
    """ 응답 받고 소비 혹은 저장하는 상태 (사용자)"""

    # init 값은 0이므로 실행, event.set()이 호출되면 1이 되기 때문에 실행되지 않음
    while not event.is_set() or not queue.empty():
        msg = queue.get() 
        logging.info(f'{bold_red}[Consumer] {yellow}stored msg -> {msg} (size={queue.qsize()}){reset}')

    logging.info(f'{bold_red}[Consumer] {yellow}received event{reset}')


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info(f'{green}[Main] {yellow}Start{reset}')

    pipeline = queue.Queue(maxsize=10)  # maxsize 중요(적장한 크기를 설정해야 함)

    # Event flag -> 0
    event = threading.Event()

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        # 실행 시간 조정
        time.sleep(0.1)

        # set 함수는 flag를 1로 변환
        event.set()
        logging.info(f'{green}[Main] {yellow}Called set func.{reset}')

    logging.info(f'{green}[Main] {yellow}End of main func.{reset}')


if __name__ == '__main__':
    main()