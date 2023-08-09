import time




def wrapper(fun):
    def inner(*args, **kwargs):
        start = time.time()
        res = fun(*args, **kwargs)
        end = time.time()
        print("func cost:%s", end - start)
        return res

    return inner
@wrapper
def func():
    list1 = []
    for i in range(100000):
        list1.append(i)

# 调用函数
func()