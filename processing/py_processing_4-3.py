"""
Multiprocessing - Sharing state

4-1 문제 해결 방법: Array 사용

공유 변수(share_value)를 공유하는 방법
    - 단일 값인 경우 Value
    - List와 같은 형태인 경우 Array

추가적인 방법
    1. shared_memory (python >= 3.8)
    2. Manager 
"""


import os
import logging
from multiprocessing import Process, current_process, Array
from color import light_blue, yellow, reset, green


def generate_update_number(numbers):
    for i in range(len(numbers)):
        numbers[i] += 1
    print(f'{light_blue}[Child-{current_process().name}] {yellow}data -> {[x for x in numbers]}{reset}')


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    parent_process_id = os.getpid()
    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}Start{reset}')

    processes = []

    # Process share memory
    share_numbers = Array('i', range(10))
    for _ in range(1, 10):
        p = Process(target=generate_update_number, args=(share_numbers,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}Share value: {[x for x in share_numbers]}{reset}')

    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}End{reset}')


if __name__ == '__main__':
    main()