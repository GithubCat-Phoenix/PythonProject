# 肥不拉几数列
def fblj_input():
    n = int(input("请输入n："))
    fblj(n)


def fblj(n):
    dp = [0, 1]

    i = 0
    while i <= n:
        result = dp[i] + dp[i + 1]
        dp.append(result)
        i += 1
    for num in dp:
        print(num, end="\t")
        if dp.index(num) % 10 == 9:
            print("")
