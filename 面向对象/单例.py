class MusicPlayer(object):
    pass
    # 定义类属性记录对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):

        # 判断是否已经创建对象
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)