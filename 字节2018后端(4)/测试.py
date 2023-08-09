n = int(input())
w = list(map(int, input().split()))
index = list(map(lambda x: int(x) - 1, input().split()))
d = {}  # 哈希表 key:(left, right, sum)
ans = [0] * n
maxHeap = 0
for i in range(n - 1, -1, -1):
    ans[i] = maxHeap
    L, R = index[i] - 1, index[i] + 1
#     print('i', L, R)
    if L in d and R in d:
        ll, lr, s1 = d[L]
        rl, rr, s2 = d[R]
        # 删除哈希表的端点
        d.pop(lr)
        d.pop(rl)
        d[ll] = d[rr] = (ll, rr, s1 + s2 + w[index[i]])
        # 删除和更新
        maxHeap = max(maxHeap, s1 + s2 + w[index[i]])
    elif L in d:
        ll, lr, s1 = d[L]
        # 删除哈希表的端点
        d.pop(lr)
        d[ll] = d[index[i]] = (ll, index[i], s1 + w[index[i]])
        # 删除和更新
        maxHeap = max(maxHeap, s1 + w[index[i]])
    elif R in d:
        rl, rr, s2 = d[R]
        # 删除哈希表的端点
        d.pop(rl)
        d[index[i]] = d[rr] = (index[i], rr, s2 + w[index[i]])
        # 删除和更新
        maxHeap = max(maxHeap, s2 + w[index[i]])
    else:
        d[index[i]] = (index[i], index[i], w[index[i]])
        maxHeap = max(maxHeap, w[index[i]])
print('\n'.join(str(n) for n in ans))