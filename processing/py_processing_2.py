"""
Multi-Processing: PID & Process Name 

Process ID * Process Name을 뽑아서 출력
"""


import os
import random
import time
import logging
from multiprocessing import Process, current_process
from color import light_blue, yellow, reset, green


def calc_square(n):
    time.sleep(random.randint(1, 3))

    child_process_id = os.getpid()
    child_process_name = current_process().name
    print(f'{light_blue}[Child-{child_process_id}] {yellow}Name: {child_process_name}{reset}')

    res = n * n * n  # Cube volume
    print(f'{light_blue}[Child-{child_process_id}] {yellow}H{n} x W{n} x L{n} -> {res}{reset}')


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    parent_process_id = os.getpid()
    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}Start{reset}')

    processes = []

    for i in range(1, 51):
        c = Process(name=str(i), target=calc_square, args=(i,))
        processes.append(c)
        c.start()

    for process in processes:
        process.join()

    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}End{reset}')


if __name__ == '__main__':
    main()