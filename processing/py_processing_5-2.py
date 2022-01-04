"""
Multi-Processing: Pipe 

Pipe
    - 1:1로 연결(Parent <-> Child)
    - send 후 close 해야함
    - Pipe는 부모와 자식 간의 1:1 통신
    - Socket 통신 유사
"""


import time
import os
import logging
from multiprocessing import Process, current_process, Pipe 
from color import light_blue, yellow, reset, green, bold_red


def worker(baseNum, pipe):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0
    for i in range(baseNum):
        sub_total += 1
    pipe.send(sub_total)
    pipe.close()
        
    print(f'{light_blue}[Child-{process_id}] {yellow}Name: {process_name}{reset}')
    print(f'{light_blue}[Child-{process_id}] {yellow}Result: {sub_total}{reset}')


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    parent_process_id = os.getpid()
    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}Start{reset}')

    ts = time.time()

    parent_pipe, child_pipe = Pipe()

    p = Process(name='1', target=worker, args=(100000000, child_pipe))
    p.start()
    p.join()

    logging.info(f'{bold_red}{time.time() - ts:2.4f}{reset} sec')

    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}Count: {parent_pipe.recv()}{reset}')

    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}End{reset}')


if __name__ == '__main__':
    main()