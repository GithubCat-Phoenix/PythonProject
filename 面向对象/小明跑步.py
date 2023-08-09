class Human:
    def __init__(self, name, weight):
        # 姓名
        self.name = name
        # 体重
        self.weight = weight

    # 跑步减少0.5公斤
    def run(self):
        self.weight -= 0.5

    # 吃东西增加1公斤
    def eat(self):
        self.weight += 1

    def __str__(self):
        return "我的名字是%s，体重为%.1f" % (self.name, self.weight)


xiaoming = Human("小明", 75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

xiaomei = Human("小美", 45.0)
xiaomei.run()
xiaomei.eat()
print(xiaomei)