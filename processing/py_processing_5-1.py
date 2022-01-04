"""
Multi-Processing: Queue
"""


import time
import os
import logging
from multiprocessing import Process, current_process, Queue 
from color import light_blue, yellow, reset, green, bold_red


def worker(baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0
    for i in range(baseNum):
        sub_total += 1
    q.put(sub_total)
        
    print(f'{light_blue}[Child-{process_id}] {yellow}Name: {process_name}{reset}')
    print(f'{light_blue}[Child-{process_id}] {yellow}Result: {sub_total}{reset}')


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    parent_process_id = os.getpid()
    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}Start{reset}')

    processes = []

    ts = time.time()

    q = Queue()
    for i in range(5):
        p = Process(name=str(i), target=worker, args=(100000000, q))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    logging.info(f'{bold_red}{time.time() - ts:2.4f}{reset} sec')

    # flag of exiting
    q.put('exit')

    # Waiting
    total = 0
    while True:
        res = q.get()
        if res == 'exit':
            break
        else:
            total += res 

    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}Count: {total}{reset}')

    logging.info(f'{green}[Parent-{parent_process_id}] {yellow}End{reset}')


if __name__ == '__main__':
    main()