# Multi-Threading

## 실습
1. Threading 사용 방법과 Join 함수
2. Daemon
3. ThreadPoolExecutor
    1. submit
    2. map
    3. as_completed
4. Lock & DeadLock & Thread Synchronization
    1. 공유 변수 문제
    2. acquire & release
    3. with문 사용
5. Queue
    1. 무한 반복(주의)
    2. 5-1 해결

## 개념
### Process란?
> Memory 위에서 실행되고 있는 프로그램

### Thread란?
> Process 내에서 실행되는 흐름의 단위

### Multi-Threading
1. 