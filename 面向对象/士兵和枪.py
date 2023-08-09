class Soldier:

    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def fire(self):
        pass


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet = 0

    def reload(self, num):
        self.bullet += num

    def shoot(self):
        # 判断是否有子弹
        if self.bullet <= 0:
            print("%s没有子弹了..." % self.model)
            return

        # 发射子弹，数量-1
        self.bullet -= 1

        # 提示开枪信息
        print("%s fire!\n剩余子弹数量%d" % (self.model, self.bullet))


ak74m = Gun("ak74m")
ak74m.reload(30)
ak74m.shoot()

