"""
Multi-Processing: Process 예제

Child Process는 Main Process 종료 여부와 상관없이 자신이 맡은 부분을 끝까지 수행하고 끝남
Join 함수를 이용해서 Child Process가 끝날 때까지 Main Process 대기
Terminate 함수를 이용하여 Child Process를 강제 종료할 수 있음

Child Process 안에서 logging을 사용할 때는 추가적인 처리가 필요
"""


from multiprocessing import Process
import time
import logging
from color import light_blue, yellow, reset, green, bold_red


def run_proc(id):
    print(f'{light_blue}[Child-{id}] {yellow}Start{reset}')
    time.sleep(2)
    print(f'{light_blue}[Child-{id}] {yellow}End{reset}')


def main():
    # logging setting
    format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    p = Process(target=run_proc, args=('1',))

    logging.info(f'{green}[Main] {yellow}Start{reset}')
    p.start()

    # 3초를 기다리지 않고 강제 종료 할 수 있음
    # logging.info(f'{green}[Main] {yellow}terminated process{reset}')
    # p.terminate()

    logging.info(f'{green}[Main] {yellow}joined process{reset}')
    p.join()

    logging.info(f'{green}[Main] {bold_red}is alive? {p.is_alive()}{reset}')

    logging.info(f'{green}[Main] {yellow}End{reset}')


if __name__ == '__main__':
    main()