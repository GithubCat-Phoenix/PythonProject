# 队列的思想，一个set存k，然后两个指针移动，left右移set中k-- right右移k++
# 牛客对python输入及其不友好，有的输入最后有空格有的没有，这个要注意

_ = int(input())
q = [int(e) for e in input().split(' ')[:-1]]

m = int(input())

list = []
for i in range(m):
    list.append([int(e) for e in input().split(' ')])
tmp = []
for i in range(len(list)):
    tmp.append([list[i][0]-1,list[i][1]-1,list[i][2],i])
tmp = sorted(tmp,key=lambda x:x[0])

left = 1
right = -1
_dict = {}
for e in q:
    _dict[e] = 0
ret = []
for row in tmp:
    l_d = row[0] - left
    r_d = row[1] - right
    for i in range(l_d):
        _dict[q[left + i]] -= 1
    for i in range(r_d):
        _dict[q[right + i + 1]] += 1
    if row[2] in _dict:
        ret.append([_dict[row[2]],row[3]])
    else:
        ret.append([0,row[3]])
    left = row[0]
    right = row[1]
ret = sorted(ret,key=lambda x:x[1])

for e in ret:
    print(e[0])