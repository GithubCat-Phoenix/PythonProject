class Game:
    # 类属性游戏历史最高分
    top_score = 0

    # 实例属性玩家姓名
    def __init__(self, player_name):
        self.player_name = player_name

    # 静态方法
    @staticmethod
    def show_help():
        pass

    # 类方法
    @classmethod
    def show_top_score(cls):
        pass

    # 实例方法
    def start_game(self):
        pass
