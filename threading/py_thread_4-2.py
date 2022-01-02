"""
Threading 4: Lock & DeadLock & Thread Synchronization

공유 변수 문제를 해결하기 위한 방법 1
    acquire & release 사용
"""


import time
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from color import light_blue, yellow, reset, green


class FakeDatabase:
    def __init__(self):
        self.val = 0  # Shared value
        self._lock = threading.Lock()
    
    def update(self, id):
        logging.info(f'{light_blue}[Sub-{id}] {yellow}Start{reset}')

        self._lock.acquire()
        logging.info(f'{light_blue}[Sub-{id}] {yellow}acquire{reset}')

        local_copy = self.val
        local_copy += 1
        time.sleep(0.1)
        self.val = local_copy

        self._lock.release()
        logging.info(f'{light_blue}[Sub-{id}] {yellow}release{reset}')

        logging.info(f'{light_blue}[Sub-{id}] {yellow}End, Result -> {local_copy}{reset}')


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info(f'{green}[Main] {yellow}Start{reset}')

    db = FakeDatabase()

    logging.info(f'Shared value: {db.val}')

    with ThreadPoolExecutor(max_workers=2) as executor:
        for num in range(1, 4):
            executor.submit(db.update, num)

    logging.info(f'{green}[Main] {yellow}End, Result -> {db.val}{reset}')


if __name__ == '__main__':
    main()