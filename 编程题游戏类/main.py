import random


def show_menu():
    # 显示菜单
    print("=" * 24 + "游戏" + "=" * 23)
    print("1. 猜数字游戏")
    print("2. 纸牌猜大小游戏")
    print("3. 退出游戏系统")
    print("=" * 50)


def guessnum():
    num = random.randint(1, 100)
    print("欢迎来玩猜数字游戏")
    for i in range(1,11):
        guess = int(input("请输入你要猜测的数字，数字范围1-100："))
        if guess > num:
            print("数字大了")
        elif guess < num:
            print("数字小了")
        elif guess == num:
            print("恭喜你赢了！")
            return
        print(f"你已猜测{i}次，剩余次数：{10-i}")
    else:
        print("抱歉你输了！")
        return


def guesscard():
    suit = ["黑桃", "红心", "方块", "梅花"]
    num = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
    score_map = {}

    for s in suit:
        count = 2
        for n in num:
            score_map[f"{s}{n}"] = count
            count += 1
    score_map.update({"joker": 14, "Joker": 15})
    print(score_map)







while True:

    # 显示功能菜单
    show_menu()

    action_str = input("请输入你要玩的游戏：")
    print()

    print("_ " * 30)

    # 1,2,3针对名片的操作
    if action_str in ["1", "2"]:
        # 猜数字游戏
        if action_str == "1":
            guessnum()

        # 纸牌猜大小游戏
        elif action_str == "2":
            guesscard()

    # 3 退出游戏系统
    elif action_str == "3":
        print("退出系统")
        print("欢迎再来玩【游戏】")
        break

    # 输入其他内容提示错误
    else:
        print("")
        print("无效操作，请重新输入！")



