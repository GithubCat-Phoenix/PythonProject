# 记录所有的名片字典
card_list = []


def show_menu():
    # 显示菜单
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("新增名片")
    print("-" * 60)

    # 1.提示用户输入名片的详细信息

    # 判断字符是否为空
    while True:

        name_str = input("请输入姓名：").strip()

        if name_str == "":
            print("名片姓名不能为空，请重新输入!")

        else:
            break

    while True:

        phonenum_str = input("请输入电话号码：").strip()

        if phonenum_str == "":
            print("名片电话不能为空，请重新输入!")

        else:
            break

    while True:

        emailadd_str = input("请输入邮箱：").strip()

        if emailadd_str == "":
            print("名片邮箱不能为空，请重新输入!")

        else:
            break

        # 2.使用用户的提示信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phonenum_str,
                 "email": emailadd_str}
    # 3.如果有重复姓名，提示是否删除
    for find_dict in card_list:
        if find_dict["name"] == name_str:
            print("系统中已经含有姓名为%s的名片" % name_str)

            while True:

                action_str = input("是否删除新创建的同名名片？1.是 0.否\n")

                if action_str == "1":
                    print("已成功删除同名名片!")

                    return

                elif action_str == "0":
                    # 4. 将名片字典加入到列表中
                    card_list.append(card_dict)

                    print(card_dict)

                    # 5.提示用户添加成功
                    print("添加姓名为%s的名片成功!" % name_str)

                    return

                else:
                    print("无效操作，请重新输入！")

    else:
        # 将名片字典加入到列表中
        card_list.append(card_dict)

        print(card_dict)

        # 提示用户添加成功
        print("添加姓名为%s的名片成功！" % name_str)


def show_all():
    """显示所有名片"""
    print("显示全部")
    print("-" * 60)

    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何名片记录，请新建名片！")

        return

    # 打印表头
    for name in ["姓名", "电话", "邮箱"]:
        print("%-15s" % name, end="")
    print("")

    #     打印分割线
    print("=" * 35)
    #     遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%-15s\t%-15s\t%-15s" % (card_dict["name"],
                                       card_dict["phone"],
                                       card_dict["email"]))


def search_card():
    """搜索名片"""
    print("搜索名片")
    print("-" * 60)

    #     1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    #     2.遍历名片列表，查询要搜索的姓名，如果没有找到，要提示用户

    # 定义计数器

    i = 1

    # 针对相同姓名定义列表

    samename_list = []

    for card_dict in card_list:

        if card_dict["name"] == find_name:

            #  处理同姓名的名片
            if i < 2:
                for name in ["姓名", "电话", "邮箱"]:
                    print("%-15s" % name, end="")
                print("")

                #     打印分割线
                print("=" * 35)

                # 计数器加一
                i += 1

            print("%-15s\t%-15s\t%-15s" % (card_dict["name"],
                                           card_dict["phone"],
                                           card_dict["email"]))
            samename_list.append(card_dict)

            # TODO 针对找到的名片执行修改和删除操作

    else:
        if i == 1:
            print("抱歉，没有找到姓名为%s的名片！" % find_name)

        if i != 1:
            del_card(samename_list)
            return

        while True:

            action_str = input("请输入【0】返回主菜单！")

            if action_str != "0":
                print("无效操作，请重新输入！")

            elif action_str == "0":
                break


def del_card(find_list):
    print(find_list)

    while True:

        action_str = input("请选择想要执行的操作：1:修改名片 2:删除名片 0:返回上级菜单\n")

        # 同名名片索引
        if len(find_list) > 1:
            num = int(input("注意!共有%d个同名名片，请选择想要对第几个名片执行操作!\n" % len(find_list)))
            print("您选择对第%d个名片执行操作" % num)

        if action_str == "1":

            print("您执行的操作是：【1】修改名片")

            while True:

                newname_str = input("请输入新姓名：").strip()

                if newname_str == "":
                    print("名片姓名不能为空，请重新输入!")

                else:
                    break

            while True:

                newphonenum_str = input("请输入新电话号码：").strip()

                if newphonenum_str == "":
                    print("名片电话不能为空，请重新输入!")

                else:
                    break

            while True:

                newemailadd_str = input("请输入新邮箱：").strip()

                if newemailadd_str == "":
                    print("名片邮箱不能为空，请重新输入!")

                else:
                    break

                # 2.使用用户的提示信息建立一个名片字典
            card_dict = {"name": newname_str,
                         "phone": newphonenum_str,
                         "email": newemailadd_str}

            # 3.如果有重复姓名，提示是否删除
            for find_dict in card_list:
                if find_dict["name"] == newname_str:
                    print("系统中已经含有姓名为%s的名片" % newemailadd_str)

                    while True:

                        action_str = input("是否删除新创建的同名名片？1.是 0.否\n")

                        if action_str == "1":
                            print("已成功删除同名名片!")

                            return

                        elif action_str == "0":
                            # 4. 将名片字典加入到列表中
                            if num > 1:
                                find_list[num-1] = card_dict
                            else:
                                find_list.clear()
                                find_list.append(card_dict)
                            print(card_dict)
                            print("名片修改完成！")

                            return

                        else:

                            print("无效操作，请重新输入！")

            else:
                # 将名片字典加入到列表中
                card_list.append(card_dict)

                print(card_dict)

            print("名片修改完成！")

        #     打印表头
            for name in ["姓名", "电话", "邮箱"]:
                print("%-15s" % name, end="")
            print("")

        #     打印分割线
            print("=" * 35)

            #     遍历名片列表依次输出字典信息
            for card_dict in find_list:
                print("%-18s\t%-18s\t%-18s" % (card_dict["name"],
                                               card_dict["phone"],
                                               card_dict["email"]))

        elif action_str == "2":

            print("您执行的操作是：【2】删除名片")

            pass

            print("名片删除成功！")

            #     打印表头
            for name in ["姓名", "电话", "邮箱"]:
                print("%-15s" % name, end="")
            print("")

            #     打印分割线
            print("=" * 35)

            #     遍历名片列表依次输出字典信息
            for card_dict in find_list:
                print("%-18s\t%-18s\t%-18s" % (card_dict["name"],
                                               card_dict["phone"],
                                               card_dict["email"]))

        elif action_str == "0":

            print("您执行的操作是：【0】返回上级菜单")
            break

        else:
            print("无效操作，请重新输入！")
