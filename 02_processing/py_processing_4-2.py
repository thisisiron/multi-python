"""
Multi-Processing: Sharing state

4-1 문제 해결 방법: Value 사용

공유 변수(share_value)를 공유하는 방법
    - 단일 값인 경우 Value
    - List와 같은 형태인 경우 Array

추가적인 방법
    1. shared_memory (python >= 3.8)
    2. Manager 
"""


import os
import logging
from multiprocessing import Process, current_process, Value
from color import light_blue, yellow, reset, green


def generate_update_number(v):
    for _ in range(50):
        # share_value는 Value라는 객체이기 때문에 value라는 속성 값에 접근해야 함
        v.value += 1  
    print(f'{light_blue}[Child-{current_process().name}] {yellow}data -> {v}{reset}')


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    parent_process_id = os.getpid()
    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}Start{reset}')

    processes = []

    # Process share memory
    share_value = Value('i', 0)   # 타입을 적어야함, int -> i
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