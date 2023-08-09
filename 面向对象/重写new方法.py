class A:
    def __new__(cls, *args, **kwargs):
        print("分配空间")
        return super().__new__(cls)

    def __init__(self):
        print("欢迎使用")

    def __str__(self):
        return "end"


a = A()
print(a)