"""
Multi-Processing: Sharing state

Problem: 모든 프로세스들이 공유할 수 있는 변수(shared_value)를 만들었지만 공유를 하지 않음
    - 현재 이 코드는 공유 변수가 공유되고 있지 않음 
    - Why? 프로세스는 메모리 단에서 독립적으로 실행
"""


import os
import logging
from multiprocessing import Process, current_process
from color import light_blue, yellow, reset, green


def generate_update_number(v):
    for _ in range(50):
        v += 1
    print(f'{light_blue}[Child-{current_process().name}] {yellow}data -> {v}{reset}')


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    parent_process_id = os.getpid()
    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}Start{reset}')

    processes = []

    # Process share memory
    share_value = 0
    for _ in range(1, 10):
        p = Process(target=generate_update_number, args=(share_value,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}Share value: {share_value}{reset}')

    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}End{reset}')


if __name__ == '__main__':
    main()