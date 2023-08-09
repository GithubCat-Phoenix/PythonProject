import multiprocessing
import time


def thread_1():
    while True:
        print("进程信息")
        time.sleep(1)


def thread_2(int_1):
    while int_1 >= 1:
        time.sleep(1)
        print("进程2")
        print()
        int_1 -= 1


if __name__ == "__main__":
    t1 = multiprocessing.Process(target= thread_1)
    t2 = multiprocessing.Process(target=thread_2, args="t3")
    t1.start()
    t2.start()
