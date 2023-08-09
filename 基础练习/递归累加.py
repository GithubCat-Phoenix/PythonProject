def sum_num(num):
    if num == 1:
        return 1

    next = sum_num(num - 1)

    return next + num


num = int(input("请输入数字："))
print(sum_num(num))

