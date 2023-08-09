def exchange(char_, m):
    n = len(char_)
    ans = 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        dp[i][i + 1] = char_[i + 1] - char_[i] - 1  # 相邻两个的交换的最小次数
        if dp[i][i + 1] < m:
            ans = 2
    for leng in range(2, n):
        for i in range(0, n - leng):
            j = leng + i
            dp[i][j] = dp[i + 1][j - 1] + (char_[j] - char_[i]) - (j - i - 1)
            if dp[i][j] < m:
                ans = leng + 1
    return ans


if __name__ == "__main__":
    exchange("13213",1)

s, m = input().split()
m = int(m)
char = [[] for _ in range(26)]  # 记录字符串中每一字母的位置
for i in range(len(s)):
    char[ord(s[i]) - 97].append(i)
res = 0
for i in range(26):
    if char[i]:
        res = max(res, exchange(char[i], m))
print(res)
