"""
Threading 4: Lock & DeadLock & Thread Synchronization

Mission: 2개의 Thread로 3개의 작업(val을 +1 하는 작업)을 수행
Result: FakeDatabase에 있는 val 값은 2가 출력, 원하던 val 값은 3이어야 함

원인: 
    Sub-1, Sub-2는 각자 수행이 되기 때문에 각자 val 값을 +1 수행
    id가 3인 Sub-3은 Sub-1 혹은 Sub-2가 끝난 이후에 진행이 되기 때문에 
    값이 1인 val 값에 +1을 하여 2를 출력 
"""

import time
import logging
from concurrent.futures import ThreadPoolExecutor
from color import light_blue, yellow, reset, green


class FakeDatabase:
    def __init__(self):
        self.val = 0  # Shared value
    
    def update(self, id):
        logging.info(f'{light_blue}[Sub-{id}] {yellow}Start{reset}')

        local_copy = self.val
        local_copy += 1
        time.sleep(0.1)

        self.val = local_copy

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