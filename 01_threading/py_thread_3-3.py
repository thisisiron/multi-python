"""
Threading 3: ThreadPoolExecutor, as_completed

submit 함수
1. 각 task에 맞게 여러 arguments를 다양한 function에 전달 가능
2. 순서 보장 X (map함수는 전달한 순서대로 결과 반환)
3. 반환 값의 타입은 Future (as_compleated, wait 등 함수 혹은 여러 설정이 가능)

ThreadPoolExecutor을 with로 이용하여 실행
"""


import time
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from color import light_blue, yellow, reset, green


def do(id, r):
    logging.info(f'{light_blue}[Sub-{id}] {yellow}Start{reset}')

    total = 0
    for i in r:
        total += i

    logging.info(f'{light_blue}[Sub-{id}] {yellow}End, Result: {total}{reset}')
    return total


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info(f'{green}[Main] {yellow}Start{reset}')

    ts = time.time()
    with ThreadPoolExecutor(max_workers=3) as executor:
        jobs = [executor.submit(do, id, r) for id, r in zip(['1', '2', '3', '4'], [range(101), range(1001), range(10001), range(100001)])]

        for job in as_completed(jobs):
            result = job.result()
            
            logging.info(f'{green}[Main] {yellow}Result of jobs -> {result}{reset}')
    print(f'{time.time() - ts} sec')

    logging.info(f'{green}[Main] {yellow}End{reset}')


if __name__ == '__main__':
    main()